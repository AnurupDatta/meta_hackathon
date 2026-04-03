# 🌱 AgriAgent Arena (OpenEnv Compatible)

An interactive **Reinforcement Learning (RL) environment** for smart farming, built using **Gym standards + OpenEnv format**, where multiple agents compete to optimize crop health.
<img width="2879" height="1551" alt="image" src="https://github.com/user-attachments/assets/ca5f4783-4b07-42f5-a683-96bf752d15bf" />
<img width="2879" height="1548" alt="image" src="https://github.com/user-attachments/assets/38564c68-4a64-4b52-ba0d-093ae9409e30" />

---

## 🚀 Project Overview

**AgriAgent Arena** is a simulation environment where AI agents learn to manage a farm by taking actions such as:

* 💧 Irrigation
* 🧪 Pest Control
* 🌿 Fertilization

Each decision affects the environment and produces a **reward**, allowing agents to optimize their strategies over time.

---

## 🧠 Key Highlights

### ✅ OpenEnv + Gym Compatible

* Fully follows **Gym-style API**
* Supports:

  * `reset()`
  * `step(action)`
  * `action_space`
  * `observation_space`
* Ready for OpenEnv evaluation

---

### 🤖 Multi-Agent System

* 👤 Human-controlled agent
* 🚜 Irrigation agent (rule-based)
* 🎲 Random agent
* 🧠 PPO-style intelligent agent

---

### 📊 Real-Time Visualization

* Multi-agent reward comparison graph
* 🥇 Best agent automatically highlighted
* Performance tracking across episodes

---

### 🏆 Leaderboard System

* Tracks agent performance
* Displays top-performing agent
* Updates dynamically

---

### 🎮 Interactive Dashboard

Built using **Gradio UI**:

* Environment state visualization
* Action controls
* Reward tracking
* Leaderboard display

---

## ⚙️ Environment Design

### 🔄 RL Loop

```bash
State → Action → Reward → New State → Repeat
```

---

### 📥 State (Observation Space)

```bash
[soil_moisture, crop_health, pest_level]
```

* Range: 0 – 100

---

### 🎯 Actions (Action Space)

| Action | Description  |
| ------ | ------------ |
| 0      | 💧 Irrigate  |
| 1      | 🧪 Spray     |
| 2      | 🌿 Fertilize |

---

### 🏆 Reward Function

```bash
Reward = Crop Health - Pest Level
```

👉 Goal: Maximize crop health while minimizing pests

---

## 🏗️ Project Structure

```bash
agri-agent-arena/
│
├── app.py                  # Main FastAPI app
│
├── api/
│   └── routes.py           # API endpoints
│
├── env/
│   └── crop_env.py         # OpenEnv-compatible environment
│
├── agents/
│   ├── basic_agents.py     # Rule-based agents
│   └── ppo_agent.py        # PPO-style policy agent
│
├── utils/
│   ├── leaderboard.py      # Ranking system
│   └── plotting.py         # Visualization logic
│
├── ui/
│   └── gradio_ui.py        # Interactive dashboard
│
├── openenv.yaml            # OpenEnv configuration ⭐
├── Dockerfile              # Container setup ⭐
├── requirements.txt
└── README.md
```

---

## 🧪 How to Run Locally

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/agri-agent-arena.git
cd agri-agent-arena
```

---

### 2️⃣ Create Environment

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

### 4️⃣ Run Server

```bash
uvicorn app:app --reload
```

---

### 5️⃣ Open UI

👉 Open in browser:

```bash
http://127.0.0.1:8000/ui
```

---

## 🎮 How to Use

1. Click **Reset**
2. Try:

   * 👤 Manual actions
   * 🤖 AI agents
3. Observe:

   * 📊 Reward graph
   * 🏆 Leaderboard
   * 🥇 Best agent

---

## 🧠 PPO Agent Strategy

The PPO-style agent uses a simple policy:

* High pest → 🧪 Spray
* Low soil → 💧 Irrigate
* Otherwise → 🌿 Fertilize

---

## 📊 Expected Results

| Agent        | Performance |
| ------------ | ----------- |
| 🧠 PPO Agent | Best 📈     |
| 🎲 Random    | Unstable    |
| 🚜 Irrigate  | Suboptimal  |

---

## 🌍 Real-World Applications

* Smart Agriculture 🌾
* Resource Optimization 💧
* Autonomous AI Systems 🤖
* RL Research & Experimentation

---

## 🚀 Deployment (Hugging Face Spaces)

This project is fully ready for deployment:

* ✅ Dockerized
* ✅ OpenEnv compatible
* ✅ UI ready

👉 Deploy using **Gradio + Docker** on Hugging Face Spaces

---

## 🏆 Hackathon Alignment

This project satisfies:

* ✅ RL Environment Design
* ✅ OpenEnv Compatibility
* ✅ Reward Engineering
* ✅ Interactive Visualization
* ✅ Scalable Architecture

---

## 🔮 Future Improvements

* 🧠 Real PPO training (Stable-Baselines3)
* 📊 Live training graphs
* 💾 Persistent leaderboard (database)
* 🎯 Scenario-based simulations

---

## 👨‍💻 Author (Anurup Datta)

* Application Developer
* AI Engineer

