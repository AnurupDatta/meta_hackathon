import random

def run_basic_agent(env, agent_histories, agent_name, strategy):
    state = env.reset()
    done = False
    total_reward = 0

    agent_histories[agent_name] = []

    while not done:
        if strategy == "random":
            action = random.randint(0, 2)
        else:
            action = strategy

        state, reward, done, _ = env.step(action)
        agent_histories[agent_name].append(reward)
        total_reward += reward

    return state, total_reward