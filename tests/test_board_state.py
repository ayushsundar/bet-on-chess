import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.board_state import get_board_after_moves, get_basic_features
from src.data_loader import load_games, get_moves_from_game
def test_board_state():
    game = next(load_games("/Users/ayush/Downloads/carlsen_randjelovic_1999.pgn"))
    moves = get_moves_from_game(game)
    curr_board = get_board_after_moves(moves)
    basic_features = get_basic_features(curr_board)

    print(curr_board)
    print("Basic Game Statistics:", basic_features)

if __name__ == "__main__":
    test_board_state()