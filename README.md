# ♟️ bet-on-chess

This project is my attempt to predict what move Magnus Carlsen would play in any given chess position.

The goal isn’t to build a full betting platform (at least not yet), but to get a model that can output the top 5 most likely moves Magnus might play, with probabilities. It’s a mix of chess, modeling, and trying to capture player style in a way that feels fun to explore.

---

## 🧠 Why I'm Doing This

I like projects where I can combine things I care about — in this case, chess, prediction, and understanding how people make decisions. Chess already has great engines, but they don’t tell you how Magnus *thinks*. This is just a way for me to explore that idea and see how far I can get.

---

## ✅ What I’ve Done

- Parsed thousands of Magnus’s games from PGNs
- Built a full feature extractor to turn board states into numeric input
- Used Stockfish to annotate positions with evaluation data
- Clustered similar board positions to group decision patterns
- Trained a model to predict what move Magnus would likely play
- Evaluated performance using top-1 and top-3 accuracy
- Got a baseline model working with about 11% top-1 and 21% top-3 accuracy

---

## 🔨 Tools and Stack

- Python, Scikit-learn, LightGBM, NumPy, Matplotlib
- PGN parsing with `python-chess`
- Stockfish for evaluation
- Jupyter notebooks for exploration

---

## 🚧 What’s Left

- Add better features (threats, king safety, piece activity)
- Handle low-frequency moves more gracefully (maybe reweight or oversample)
- Possibly train separate models per cluster
- Visualize predictions on live boards
- Keep tuning and testing — just curious how good this can get

---

This is just something I’m doing because I find it fun and interesting. I’ll keep updating it as I go.
