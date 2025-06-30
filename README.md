# bet-on-chess
TL;DR Predicting Magnus Carlsen's next move using machine learning and board state analysis.

This project is my attempt to predict what move Magnus Carlsen would play in any given chess position.

The goal isn’t to build a full betting platform (at least not yet), but to get a model that can output the top 5 most likely moves Magnus might play, with probabilities. It’s a mix of chess, modeling, and trying to capture player style in a way that feels fun to explore.

---

## Why I'm Doing This

I like projects where I can combine things I care about. In this case, it's chess, prediction, and understanding how people make decisions. Chess already has great engines, but they don’t tell you how Magnus thinks. This is just a way for me to explore that idea and see how far I can get.

---

## What I’ve Done

- Parsed 884,445 positions from Magnus’s games using PGN files  
- Built a feature extractor to turn board states into numeric input  
- Annotated each position with Stockfish evaluations  
- Extracted and saved a cleaned dataset of 883,935 usable positions  
- Clustered similar board positions to explore stylistic groupings  
- Trained a baseline model to predict Magnus’s next move  
- Evaluated accuracy using top-1 and top-3 prediction metrics  
- Established a working baseline with ~11% top-1 and ~21% top-3 accuracy  

---

## Tools and Stack

- Python, Scikit-learn, LightGBM, NumPy, Matplotlib  
- PGN parsing with `python-chess`  
- Stockfish for evaluation and annotation  
- Jupyter notebooks for experimentation and analysis  

---

## What’s Next

- Engineer better features (e.g., threats, king safety, piece activity)  
- Rebalance for rare or low-frequency moves  
- Test cluster-specific models to capture contextual behavior  
- Build a live board visualizer to interact with predictions  
- Continue refining and expanding the model's predictive power  
