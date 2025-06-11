# ♟️ bet-on-chess

What if you could predict Magnus Carlsen’s next move in real time?

This project explores that idea. Instead of building a full betting platform right now, the focus is on creating a model that can output the top 5 most likely moves Magnus would play in any given position, along with a probability distribution for each move.

Using historical PGN data, Stockfish evaluations, and style-aware modeling, the goal is to capture how Magnus thinks and plays, even in positions he has never seen before.

---

## 🎯 Why I'm Building This

Chess has grown massively online, but watching games is still mostly passive. I want to build a tool that lets people interact with elite-level chess more actively by predicting what a player like Magnus will do next.

Rather than just asking who will win, this project asks:

> “What will Magnus play next?”

This combines a lot of my interests, including strategy, prediction, pattern recognition, and human decision-making.

---

## 🧱 What I’m Focusing On

- Built a feature extractor to turn chess board states into numeric vectors
- Used Stockfish to evaluate move quality and board advantage
- Parsed Magnus’s historical PGN games to extract actual decisions
- Grouped similar positions into clusters to capture decision patterns
- Trained a classifier to predict likely moves in new positions
- Outputted a ranked list of the top 5 most likely moves Magnus would make in a position, with probabilities
- Blended predictions from the Magnus model with Stockfish suggestions for more reliable outputs

---

## 🔧 Tech Stack

- **Data**: PGN files from Magnus Carlsen’s games
- **Modeling**: Python, NumPy, Scikit-learn, LightGBM
- **Engine Integration**: python-chess and Stockfish
- **Tools**: Jupyter Notebooks, Matplotlib, Pickle

---

## ✅ Completed

- Built the PGN loader and move history parser
- Reconstructed board states and calculated key features
- Integrated Stockfish to evaluate positions
- Built an early odds engine using Stockfish and historical frequencies
- Created a prototype model to generate move probabilities for unseen positions

---

## 🚧 In Progress

- Expanding the feature set for board position analysis
- Training and validating the style-aware move prediction model
- Testing prediction accuracy on new games
- Blending the model with Stockfish in a smarter, context-aware way

---

Made by [@ayushsundar]
