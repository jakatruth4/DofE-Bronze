# [Project Name] - Bronze DofE 6-Month Skills Project

A real-time browser-based **chess application with WebSockets, a custom Elo rating system, and custom game variants**, built over 6 months for my **Bronze Duke of Edinburgh's Award (Skills Section)** and tracked through regular Git commits across 26 weeks.

---

## DofE Overview

* **Award Level:** Bronze
* **Section:** Skills (6-month option)
* **Timeframe:** [Start Date] - [End Date] (26 weeks, roughly 1 hour per week)
* **Assessor:** [Assessor Name and Role]

### Project Aim
To build a full-featured browser chess app with real-time WebSocket multiplayer, complete rule and draw-condition validation, a custom rating algorithm, and playable custom chess variants—refined through iterative testing over 6 months.

---

## Planned Features

* [ ] Interactive board UI in HTML/CSS/JS with legal move highlights, promotion UI, move history, and clock display
* [ ] Complete standard chess rules (castling, en passant, promotion, check/checkmate, stalemate, repetition, 50-move rule)
* [ ] Real-time WebSocket multiplayer with room codes, turn sync, and disconnect/reconnect handling
* [ ] Custom Elo rating system with persisted player ratings and rating-change history
* [ ] At least two custom chess variants with distinct rule sets and win/visibility mechanics
* [ ] Live deployment and refinements from playtesting with friends or an assessor

---

## 6-Month Roadmap

* **Month 1 - Board State and Core Rules:** Set up the repository, folder structure, UI board layout, piece movement, and legal move/check validation.
* **Month 2 - Complete Chess Rules and Move UI:** Implement castling, en passant, promotion, draw detection, algebraic notation move list, and undo/reset/review controls.
* **Month 3 - WebSockets and Real-Time Play:** Build the WebSocket server and client state sync, room/match flow, turn validation, and disconnect handling.
* **Month 4 - Custom Elo Algorithm and Persistence:** Implement baseline Elo and your custom rating formula, track rating deltas per match, and persist profiles/match records.
* **Month 5 - Custom Chess Variants:** Design, code, and test custom rule variants (such as Fog of War or piece drops/objective variants) alongside standard chess.
* **Month 6 - Playtesting, Polish, and Wrap-Up:** Run multiplayer test sessions, fix edge-case bugs, polish UI/responsiveness, add screenshots to `/docs`, and complete assessor sign-off.

---

## Tech Stack

* **Frontend:** HTML5, CSS3 (Grid/Flexbox, responsive board layout), JavaScript (ES6+ modules, WebSocket client)
* **Realtime / Server:** Node.js, WebSockets (`ws` or Socket.io)
* **Persistence and Version Control:** Git, GitHub, JSON / database or browser storage

---

## Repository Structure

```text
├── client/
│   ├── index.html          # Main application page
│   ├── css/
│   │   └── styles.css      # Board, lobby, rating, and variant UI styles
│   └── js/
│       ├── main.js         # Client entry point and UI event handlers
│       ├── board.js        # Board rendering, drag/click input, and highlights
│       ├── socket.js       # WebSocket connection, reconnection, and message handling
│       └── variant-ui.js   # Variant-specific rendering (e.g., fog of war or drop tray)
├── server/
│   ├── server.js         # WebSocket server, rooms, and session management
│   ├── engine.js         # Move generation, legality checks, and game-end rules
│   ├── elo.js            # Standard and custom Elo rating calculations
│   └── variants.js       # Custom variant rules and state modifiers
├── docs/                   # Screenshots, variant rule notes, and playtest logs
└── README.md               # Project overview and setup guide
