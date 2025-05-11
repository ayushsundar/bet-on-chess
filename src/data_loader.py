import chess.pgn # type: ignore

def load_games(path):
    with open(path, encoding = "utf-8") as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            yield game

def get_moves_from_game(game):
    board = game.board()
    moves = []
    for move in game.mainline_moves():
        moves.append(board.san(move))
        board.push(move)
    return moves