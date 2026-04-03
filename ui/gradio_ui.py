import gradio as gr
from env.crop_env import CropEnv
from agents.basic_agents import run_basic_agent
from agents.ppo_agent import run_ppo_agent
from utils.leaderboard import update_leaderboard, get_leaderboard, get_best_agent
from utils.plotting import plot_agents

ui_env = CropEnv()
agent_histories = {}

# ---------------- FUNCTIONS ---------------- #

def reset_ui():
    global ui_env, agent_histories
    ui_env = CropEnv()
    agent_histories = {}

    state = ui_env.reset()
    lb = get_leaderboard()

    return state, 0, False, None, lb, get_best_agent()


def run_agent(strategy, name):
    state, total = run_basic_agent(ui_env, agent_histories, name, strategy)

    update_leaderboard(name, total)

    lb = get_leaderboard()
    fig = plot_agents(agent_histories, lb)

    return state, total, True, fig, lb, get_best_agent()


def run_ppo():
    state, total = run_ppo_agent(ui_env, agent_histories, "Agent-PPO")

    update_leaderboard("Agent-PPO", total)

    lb = get_leaderboard()
    fig = plot_agents(agent_histories, lb)

    return state, total, True, fig, lb, get_best_agent()


# ---------------- UI ---------------- #

def create_ui():
    with gr.Blocks(theme=gr.themes.Soft()) as demo:

        # 🔥 HEADER
        gr.Markdown("""
        # 🌱 AgriAgent Arena  
        ### AI Agent Farming Simulation (OpenEnv + RL)
        """)

        # ---------------- ENVIRONMENT CARD ---------------- #
        with gr.Group():
            gr.Markdown("## 🌾 Environment State")

            state_box = gr.JSON(label="State")
            reward_box = gr.Number(label="🏆 Reward")
            done_box = gr.Textbox(label="Finished")

        # ---------------- GRAPH CARD ---------------- #
        with gr.Group():
            gr.Markdown("## 📊 Performance Graph")

            reward_plot = gr.Plot()

        # ---------------- HUMAN CONTROLS ---------------- #
        with gr.Group():
            gr.Markdown("## 👤 Human Controls")

            with gr.Row():
                btn_irrigate = gr.Button("💧 Irrigate")
                btn_spray = gr.Button("🧪 Spray")
                btn_fertilize = gr.Button("🌿 Fertilize")

        # ---------------- AI AGENTS ---------------- #
        with gr.Group():
            gr.Markdown("## 🤖 AI Agents")

            with gr.Row():
                btn_agent1 = gr.Button("🚜 Irrigate Agent")
                btn_agent2 = gr.Button("🎲 Random Agent")
                btn_ppo = gr.Button("🧠 PPO Agent")

        # ---------------- RESET ---------------- #
        with gr.Row():
            btn_reset = gr.Button("🔄 Reset", variant="primary")

        # ---------------- LEADERBOARD ---------------- #
        with gr.Group():
            gr.Markdown("## 🏆 Leaderboard")

            leaderboard_box = gr.JSON()
            best_agent_box = gr.Textbox(label="🥇 Best Agent")

        # ---------------- ACTIONS ---------------- #

        # Reset
        btn_reset.click(
            fn=reset_ui,
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        # Human actions
        btn_irrigate.click(
            fn=lambda: run_agent(0, "Human-Irrigate"),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        btn_spray.click(
            fn=lambda: run_agent(1, "Human-Spray"),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        btn_fertilize.click(
            fn=lambda: run_agent(2, "Human-Fertilize"),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        # AI agents
        btn_agent1.click(
            fn=lambda: run_agent(0, "Agent-Irrigate"),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        btn_agent2.click(
            fn=lambda: run_agent("random", "Agent-Random"),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        btn_ppo.click(
            fn=run_ppo,
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

        # Load initial leaderboard
        demo.load(
            fn=lambda: (None, None, None, None, get_leaderboard(), get_best_agent()),
            outputs=[state_box, reward_box, done_box, reward_plot, leaderboard_box, best_agent_box]
        )

    return demo