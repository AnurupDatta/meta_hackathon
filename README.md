# 🌱 AgriAgent Arena

An interactive **AI-powered farming simulation platform** where multiple agents learn and compete to optimize crop health using **Reinforcement Learning (RL)** concepts.

---

## 🚀 Project Overview

**AgriAgent Arena** simulates a smart farming environment where agents make decisions such as:

* 💧 Irrigation
* 🧪 Pest Control
* 🌿 Fertilization

Each action impacts the environment and generates a **reward**, enabling agents to improve their strategies over time.

---

## 🧠 Key Features

### 🤖 Multi-Agent System

* 👤 **Human Agent** → Manual control
* 🚜 **Agent 1** → Always irrigates
* 🎲 **Agent 2** → Random actions
* 🧠 **PPO Agent** → Smart decision-making policy

---

### 📊 Performance Visualization

* Real-time **reward graph**
* 🥇 Best agent highlighted automatically
* Easy comparison of agent performance

---

### 🏆 Leaderboard System

* Tracks agent scores
* Displays **top-performing agent**
* Updates dynamically

---

### 🎮 Interactive UI

Built using **Gradio**, featuring:

* Environment state display
* Action controls
* Performance graph
* Leaderboard

---

### ⚙️ OpenEnv-style API

* `/reset` → Initialize environment
* `/step` → Take action
* `/leaderboard` → View rankings

---

## 🏗️ Project Structure

```
agri-agent-arena/
│
├── app.py                  # Main FastAPI app
│
├── api/
│   └── routes.py           # API endpoints
│
├── env/
│   └── crop_env.py         # Environment simulation
│
├── agents/
│   ├── basic_agents.py     # Rule-based agents
│   └── ppo_agent.py        # Smart PPO-style agent
│
├── utils/
│   ├── leaderboard.py      # Ranking system
│   └── plotting.py         # Graph visualization
│
├── ui/
│   └── gradio_ui.py        # Interactive dashboard
│
├── requirements.txt
└── Dockerfile
```

---

## ⚙️ How It Works

### 🔄 Reinforcement Learning Loop

```
State → Action → Reward → New State → Repeat
```

* **State** → Soil moisture, Crop health, Pest level
* **Action** → Irrigate / Spray / Fertilize
* **Reward** → Crop Health - Pest Level

---

## 🧪 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/agri-agent-arena.git
cd agri-agent-arena
```

---

### 2️⃣ Create Virtual Environment

```bash
conda create -n agri python=3.10
conda activate agri
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Server

```bash
uvicorn app:app --reload
```

---

### 5️⃣ Open the UI

👉 Open in browser:

```
http://127.0.0.1:8000/ui
```

---

## 🎮 How to Use

1. Click **Reset**
2. Try:

   * 👤 Human actions
   * 🤖 AI agents
3. Observe:

   * 📊 Reward graph
   * 🏆 Leaderboard
   * 🥇 Best agent

---

## 🧠 PPO Agent (Smart Strategy)

The PPO-style agent uses a **state-based decision policy**:

* High pest → 🧪 Spray
* Low soil → 💧 Irrigate
* Otherwise → 🌿 Fertilize

---

## 📊 Example Behavior

* 🧠 PPO Agent → Highest reward 📈
* 🎲 Random Agent → Unstable 📉
* 🚜 Irrigate Agent → Suboptimal

---

## 🌍 Real-World Applications

* Smart Agriculture 🌾
* Resource Optimization 💧
* Autonomous AI Systems 🤖
* Decision Intelligence Platforms

---

## 🚀 Future Improvements

* ✅ Real PPO training (Stable-Baselines3)
* 📊 Live training visualization
* 💾 Persistent leaderboard (database)
* 🌐 Hugging Face Spaces deployment

---

## 🏆 Hackathon Value

This project demonstrates:

* Reinforcement Learning concepts
* Multi-agent comparison
* Real-time visualization
* API + UI integration
* Scalable architecture

---

## 👨‍💻 Author

**Anurup Datta**

* Full Stack Developer
* AI & Data Science Enthusiast

---
