import chess # type: ignore

# Applies a list of moves onto a new board and return the current board state
def get_board_after_moves(moves):
    board = chess.Board()
    for move in moves:
        board.push_san(move)
    return board

# Calculating some very basic features to make sure I'm able to access informaiton from off of a PGN file chess game
def get_basic_features(board):
    white_material = sum([len(board.pieces(piece_type, chess.WHITE)) for piece_type in range(1,7)])
    black_material = sum([len(board.pieces(piece_type, chess.BLACK)) for piece_type in range(1,7)])
    num_legal_moves = board.legal_moves.count()
    if board.turn == chess.WHITE:
        turn = "White to move"
    else:
        turn = "Black to move"

    return{
        'Material_balance for white': white_material,
        'Material_balance for black': black_material,
        '# Of Legal Moves': num_legal_moves,
        'Player to move': turn
    }