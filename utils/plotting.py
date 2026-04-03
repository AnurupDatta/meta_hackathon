import matplotlib.pyplot as plt

def plot_agents(agent_histories, leaderboard=None):
    """
    Plots reward curves for all agents and highlights the best agent.

    Args:
        agent_histories (dict): {agent_name: [reward1, reward2, ...]}
        leaderboard (list): [(agent_name, avg_score), ...]
    """

    # If no data, return nothing
    if not agent_histories:
        return None

    plt.figure()

    # ---------------- FIND BEST AGENT ---------------- #
    best_agent = None
    if leaderboard and len(leaderboard) > 0:
        best_agent = leaderboard[0][0]

    # ---------------- PLOT ---------------- #
    for agent, rewards in agent_histories.items():

        # 🥇 Highlight best agent
        if agent == best_agent:
            plt.plot(
                rewards,
                label=f"{agent} 🥇",
                linewidth=3,        # Thick line
                marker="o",         # Points
                markersize=6
            )
        else:
            plt.plot(
                rewards,
                label=agent,
                linestyle="--",     # Dashed
                alpha=0.6           # Faded
            )

    # ---------------- LABELS ---------------- #
    plt.xlabel("Steps")
    plt.ylabel("Reward")
    plt.title("📊 Multi-Agent Comparison")

    # ---------------- LEGEND ---------------- #
    plt.legend()

    # ---------------- GRID (optional nice touch) ---------------- #
    plt.grid(True, linestyle="--", alpha=0.5)

    return plt