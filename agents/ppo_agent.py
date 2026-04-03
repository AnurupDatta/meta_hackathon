def ppo_policy(state):
    soil, health, pest = state

    if pest > 30:
        return 1
    elif soil < 40:
        return 0
    else:
        return 2

def run_ppo_agent(env, agent_histories, agent_name):
    state = env.reset()
    done = False
    total_reward = 0

    agent_histories[agent_name] = []

    while not done:
        action = ppo_policy(state)
        state, reward, done, _ = env.step(action)
        agent_histories[agent_name].append(reward)
        total_reward += reward

    return state, total_reward