import chess.pgn # type: ignore

# Will be able to load in any number of games in at once, but do it one by one so they can all be used individually
def load_games(path):
    with open(path, encoding = "utf-8") as pgn:
        while True:
            game = chess.pgn.read_game(pgn)
            if game is None:
                break
            yield game

# Returns a list of SAN moves from a chess game object
def get_moves_from_game(game):
    board = game.board()
    moves = []
    for move in game.mainline_moves():
        moves.append(board.san(move))
        board.push(move)
    return moves