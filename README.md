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
│
├── assets/ # Images, sounds, icons
├── database/ # SQLite setup and queries
├── dashboard/ # Analytics visualizations
├── game/ # Main game code
│ ├── main.py # Game loop
│ └── tank.py # Tank class
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
