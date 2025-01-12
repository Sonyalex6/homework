import numpy as np
alpha = 0.1
gamma = 0.9
epsilon = 0.1
episodes = 1000
grid_size = 5
actions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Q = np.zeros((grid_size, grid_size, len(actions)))
def choose_action(state):
    if np.random.rand() < epsilon:
        return np.random.randint(len(actions))
    else:
        return np.argmax(Q[state])
def step(state, action):
    next_state = (state[0] + actions[action][0], state[1] + actions[action][1])
    if next_state[0] < 0 or next_state[0] >= grid_size or next_state[1] < 0 or next_state[1] >= grid_size:
        next_state = state
    reward = 1 if next_state == (grid_size-1, grid_size-1) else -0.1
    done = next_state == (grid_size-1, grid_size-1)
    return next_state, reward, done
def update_q(state, action, reward, next_state):
    best_next_action = np.argmax(Q[next_state])
    td_target = reward + gamma * Q[next_state][best_next_action]
    td_error = td_target - Q[state][action]
    Q[state][action] += alpha * td_error
for episode in range(episodes):
    state = (0, 0)
    done = False
    while not done:
        action = choose_action(state)
        next_state, reward, done = step(state, action)
        update_q(state, action, reward, next_state)
        state = next_state
policy = np.argmax(Q, axis=2)
print("Оптимальная политика:")
print(policy)
import matplotlib.pyplot as plt
value_function = np.max(Q, axis=2)
plt.figure(figsize=(10, 6))
plt.subplot(1, 2, 1)
plt.title('Политика')
plt.imshow(policy, cmap='viridis', origin='upper')
for i in range(grid_size):
    for j in range(grid_size):
        plt.text(j, i, policy[i, j], ha='center', va='center', color='white')
plt.subplot(1, 2, 2)
plt.title('Функция ценности')
plt.imshow(value_function, cmap='viridis', origin='upper')
for i in range(grid_size):
    for j in range(grid_size):
        plt.text(j, i, round(value_function[i, j], 2), ha='center', va='center', color='white')

plt.show()
def update_sarsa_q(state, action, reward, next_state, next_action):
    td_target = reward + gamma * Q[next_state][next_action]
    td_error = td_target - Q[state][action]
    Q[state][action] += alpha * td_error
Q = np.zeros((grid_size, grid_size, len(actions)))
for episode in range(episodes):
    state = (0, 0)
    action = choose_action(state)
    done = False
    while not done:
        next_state, reward, done = step(state, action)
        next_action = choose_action(next_state)
        update_sarsa_q(state, action, reward, next_state, next_action)
        state, action = next_state, next_action
policy_sarsa = np.argmax(Q, axis=2)
print("Оптимальная политика (SARSA):")
print(policy_sarsa)
def update_sarsa_q(state, action, reward, next_state, next_action):
    td_target = reward + gamma * Q[next_state][next_action]
    td_error = td_target - Q[state][action]
    Q[state][action] += alpha * td_error
Q = np.zeros((grid_size, grid_size, len(actions)))
for episode in range(episodes):
    state = (0, 0)
    action = choose_action(state)
    done = False
    while not done:
        next_state, reward, done = step(state, action)
        next_action = choose_action(next_state)
        update_sarsa_q(state, action, reward, next_state, next_action)
        state, action = next_state, next_action
policy_sarsa = np.argmax(Q, axis=2)
print("Оптимальная политика (SARSA):")
print(policy_sarsa)
