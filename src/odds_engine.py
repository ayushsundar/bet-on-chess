import chess.engine
import numpy as np
import pickle

def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum()

def get_top_moves_with_odds(board, stockfish_path, magnus_model_path, top_n=3, depth=15):
    
    # Connecting to Stockfish & getting the top Stockfish moves
    engine = chess.engine.SimpleEngine.popen_uci(stockfish_path)
    info = engine.analyse(board, chess.engine.Limit(depth=depth), multipv=top_n)
    stockfish_moves = []
    stockfish_scores = []

    for entry in info:
        move = entry["pv"][0]
        score = entry["score"].relative.score(mate_score=10000) # Centipawn score
        
        if score is None:
            score = 0
        stockfish_moves.append(board.san(move))
        stockfish_scores.append(score)
    # Converting the Stockfish scores to probabilities
    stockfish_probs = softmax(np.array(stockfish_scores))
    
    # Loading Magnus move freq
    with open(magnus_model_path, "rb") as f:
        magnus_move_probs_dict = pickle.load(f)
    fen = board.fen()
    magnus_probs = magnus_move_probs_dict.get(fen, {})

    # Creating blended probabilites using Magnus move freq & stockfish
    final_probs = {}

    for i, move in enumerate(stockfish_moves):
        stockfish_prob = stockfish_probs[i]
        magnus_prob = magnus_probs.get(move, 1e-6) # Super small probability if move not seen before

        # 70% Magnus 30% Stockfish
        final_probs[move] = 0.7 * magnus_prob + 0.3 * stockfish_prob

    # Normalizing final probabilities
    total = sum(final_probs.values())
    for move in final_probs:
        final_probs[move] /= total
    
    engine.quit()
    return final_probs
