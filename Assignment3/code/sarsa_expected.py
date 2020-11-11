import numpy as np

import helper
from gridworld import Gridworld

# Implementation of Expected Sarsa agent
class SarsaExpected(Gridworld):

	# Initialize the agent and the world
	def __init__(self, epsilon=0.1, alpha=0.5, gamma=1, seed=0, num_actions=4, rows=7, cols=10, start=(3, 0), end=(3, 7)):
		# Initialize the gridworld
		super().__init__(rows, cols, start, end)
		self.epsilon = epsilon
		self.alpha = alpha
		self.gamma = gamma
		self.num_actions = num_actions
		self.Q = np.zeros((self.rows * self.cols, self.num_actions))
		# Random number generator
		self.rg = np.random.default_rng(seed=seed)

	# Choose the action based on epsilon-greedy policy and current state
	def nextAction(self, state):
		if self.rg.uniform() < self.epsilon:
			return self.rg.integers(self.num_actions)
		else:
			return np.argmax(self.Q[state, :])

	def run(self, timesteps=10000, verbose=False):
		episode, t = 0, 0
		# Start with the starting state
		state = self.start
		# Episodes data for the plot
		i = 0
		data = np.zeros((timesteps // 100, 1))
		for timestep in range(timesteps):
			# Take the action corresponding to the state
			action = self.nextAction(state)
			t += 1
			
			# Verbose output 
			if verbose:
				print(f'{state}, {self.actions[action]}')
			
			# Add episodes for the plot 
			if timestep % 100 == 0:
				data[i] = episode
				i += 1

			# Epsiode ends if end state is reached
			if state == self.end:
				if verbose:
					print(f'Episode {episode} completed in {t} timesteps')
				state = self.start
				episode += 1
				t = 0
				continue

			# Find the next state based on the action taken
			next_state = self.nextState(state, action)
			# Get the reward for the current action
			reward = self.getReward(next_state)
			# Update the Q values
			self.Q[state][action] += self.alpha * (reward + self.gamma * np.mean(self.Q[next_state], axis=0) - self.Q[state][action])
			
			# Update the state
			state = next_state

		print(f'Total number of episodes completed: {episode}')
		return data