# ♟️ bet-on-chess

This is a project I’ve been wanting to build for a while. The idea is simple: what if you could bet on what move a chess player is going to make next?

Not just who wins or loses, but move-by-move predictions in real time. I’m starting with a focus on one player, probably Magnus, and trying to build a model that can predict his most likely next move given the current position. The goal is to emulate his playstyle using engine evaluations, past games, and some probability modeling.

## 🎯 Why I'm Building This

Chess has blown up online, but watching games is still mostly passive. I want to create a way for people to engage with the game more deeply by putting their intuition to the test. If you think you know Magnus better than Stockfish, now you can prove it.

This project brings together things I care about: strategy, data, prediction, and real-time decision making.

## 🧱 What I’m Planning

- Build a model that predicts the next move Magnus would play in a given position
- Generate dynamic odds based on those probabilities
- Let people place play-money bets on what they think the next move will be
- Eventually expand to other players and live games

## 🔧 Tech Stack (planned)

- **Frontend**: React and Tailwind
- **Backend**: FastAPI
- **Modeling**: Python with Stockfish
- **Data**: PGN files from historical games
- 
## ✅ Completed
- [x] Built the foundation of the data pipeline to load PGN files, extract move histories, convert them into board states, and calculate basic variables like the material count for each player and the number of legal moves they have.

## 🚧 In Progress

- [ ] Clean Magnus game data
- [ ] Create move prediction model using Stockfish eval and past behavior
- [ ] Build basic betting interface
- [ ] Run simulations on archived games

---
