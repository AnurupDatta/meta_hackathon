leaderboard = {}

def update_leaderboard(agent_name, reward):
    if agent_name not in leaderboard:
        leaderboard[agent_name] = []
    leaderboard[agent_name].append(reward)

def get_leaderboard():
    avg_scores = {
        agent: sum(scores)/len(scores)
        for agent, scores in leaderboard.items()
    }
    return sorted(avg_scores.items(), key=lambda x: x[1], reverse=True)

def get_best_agent():
    lb = get_leaderboard()
    if not lb:
        return "No agents yet"
    name, score = lb[0]
    return f"🥇 Best Agent: {name} (Score: {score:.2f})"