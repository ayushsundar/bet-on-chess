import chess.pgn

def load_games(path):
    with open(path, encoding = "utf-8") as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            yield game