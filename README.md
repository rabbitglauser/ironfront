# 🛡️ IronFront - Top-Down Tank Game

![IronFront](assets/banner.png)

**IronFront** is a 2D top-down tank game built in Python using `pygame`, inspired by tactical warfare games like *War Thunder*. Engage in explosive tank battles, dodge enemy fire, and upgrade your arsenal. Also features full database tracking and dashboard analytics.

---

## 🎮 Features

- 🔥 Smooth tank controls (WASD + mouse aiming)
- 💣 Realistic shooting, collisions, and explosions
- 🧠 Smart AI enemies (patrolling, hunting, dodging)
- 🎯 Score tracking, kills, deaths, hit accuracy
- 📊 Connected to a database (SQLite or Firebase)
- 📈 Optional analytics dashboard using Matplotlib or Flask

---
## 🎨 Assets Credits

- **Top-Down Tanks** by Kenney.nl
  - [Download from OpenGameArt.org](https://opengameart.org/content/top-down-tanks-redux)
  - License: CC0 (No attribution required)

- **Free 2D Battle Tank Game Assets** by CraftPix.net
  - [Download from CraftPix.net](https://craftpix.net/freebies/free-2d-battle-tank-game-assets/)
  - License: Free for personal and commercial use (check site for details)

- **Topdown Tanks** by Kenney.nl
  - [Download from OpenGameArt.org](https://opengameart.org/content/topdown-tanks)
  - License: CC0 (No attribution required)

- **Free Tank** by Game Developer Studio
  - [Download from Game Developer Studio](https://www.gamedeveloperstudio.com/graphics/viewgraphic.php?item=1l4m333l6u0b385o8f&page-name=Free-tank)
  - License: Check site for details

---
## 🧪 Screenshots

### 🪖 Gameplay
![Gameplay](assets/screenshot_gameplay.png)

### 📊 Dashboard Example
![Dashboard](assets/screenshot_dashboard.png)

---

## 🛠️ Tech Stack

- **Python**
- **pygame** – game engine
- **SQLite** or **Firebase** – player & match storage
- **Matplotlib / Pandas** – statistics dashboard
- **Flask (optional)** – web-based dashboard

---

## 🗂️ Project Structure
ironfront/
├── assets/
│   ├── tanks/
│   │   ├── player_tank.png
│   │   └── enemy_tank.png
│   ├── bullets/
│   │   └── bullet.png
│   ├── explosions/
│   │   └── explosion.png
│   ├── terrain/
│   │   ├── grass_tile.png
│   │   └── road_tile.png
│   └── ui/
│       ├── health_bar.png
│       └── score_panel.png
├── game/
│   └── main.py
├── README.md
└── requirements.txt


---

## 🚀 Getting Started

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/ironfront.git
cd ironfront

# Set up environment
pip install -r requirements.txt

# Run the game
python game/main.py
