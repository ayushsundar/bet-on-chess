import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.data_loader import load_games

def test_load_games():
    games = list(load_games("/Users/ayush/Downloads/carlsen_randjelovic_1999.pgn"))
    print(f"Loaded {len(games)} games.")

if __name__ == "__main__":
    test_load_games()