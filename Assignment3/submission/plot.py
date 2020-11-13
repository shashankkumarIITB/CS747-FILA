import numpy as np

import helper
from sarsa import Sarsa
from qlearning import QLearning
from sarsa_expected import SarsaExpected

# File to run in order to generate all the plots sequentially 
if __name__ == '__main__':
	data_X = np.arange(start=0, stop=10000, step=100)

	# Agent 1: Sarsa(0)
	data_Y1 = np.zeros((100, 1))
	for seed in range(50):
		print(f'Seed: {seed}')
		sarsa = Sarsa(seed=seed, num_actions=4, alpha=0.1)
		y = sarsa.run()
		data_Y1 += y
	data_Y1 /= 10
	helper.plotSingle(data_X, data_Y1, "Sarsa(0)")

	# Sarsa(0) with King's move
	data_Y2 = np.zeros((100, 1))
	for seed in range(50):
		print(f'Seed: {seed}')
		sarsa = Sarsa(seed=seed, num_actions=8, alpha=0.1)
		y = sarsa.run()
		data_Y2 += y
	data_Y2 /= 10
	helper.plotSingle(data_X, data_Y2, "Sarsa(0) with King's move")

	# Sarsa(0) with stochastic wind
	data_Y3 = np.zeros((100, 1))
	for seed in range(50):
		print(f'Seed: {seed}')
		sarsa = Sarsa(seed=seed, num_actions=4, stochastic=True, alpha=0.1)
		y = sarsa.run()
		data_Y3 += y
	data_Y3 /= 10
	helper.plotSingle(data_X, data_Y3, "Sarsa(0) with King's move and stochastic wind")
	
	# Plot comparision for different scenarios with Sarsa agent
	data_Y = [data_Y1, data_Y2, data_Y3]
	helper.plotComparision(data_X, data_Y, role='1')

	# Agent 2: Q-learning
	data_Y4 = np.zeros((100, 1))	
	for seed in range(50):
		print(f'Seed: {seed}')
		sarsa = QLearning(seed=seed, alpha=0.1)
		y = sarsa.run()
		data_Y4 += y
	data_Y4 /= 10

	# Agent 3: Expected-Sarsa
	data_Y5 = np.zeros((100, 1))	
	for seed in range(50):
		print(f'Seed: {seed}')
		sarsa = SarsaExpected(seed=seed, alpha=0.1)
		y = sarsa.run()
		data_Y5 += y
	data_Y5 /= 10

	# Plot comparision for different agents
	data_Y = [data_Y1, data_Y4, data_Y5]
	helper.plotComparision(data_X, data_Y, role='2')