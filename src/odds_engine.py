import chess.engine

engine = chess.engine.SimpleEngine.popen_uci("/Users/ayush/Downloads/stockfish/stockfish-macos-m1-apple-silicon")
board = chess.Board()
result = engine.analyse(board, chess.engine.Limit(depth=15))
keys_list = list(result.keys())
print(keys_list)
print(result['pv'])

engine.quit()