# python3 bandit.py --instance ./instances/i-2.txt --algorithm thompson-sampling--randomSeed 42 --verbose --horizon 100000

import operator, random
import numpy as np
from helper import getReward, getRegret

# Return the arm with maximum sampled value as per Beta disribution
def sampleArm(rewards, failures):
	a = np.array(list(rewards.values()))
	b = np.array(list(failures.values()))
	samples_beta = np.random.beta(a + 1, b + 1)
	arm_max = np.argmax(samples_beta)
	return arm_max + 1

# Function for epsilon-greedy sampling algorithm
def thompsonSampling(seed, horizon, means_true, verbose=False):
	np.random.seed(seed)
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	failures = {i: 0 for i in means_true.keys()}

	# Sample bandit-arms
	for _ in range(horizon):
		arm = sampleArm(rewards, failures)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		failures[arm] += 1 - reward
	
	if verbose:
		# Compute empirical means
		means_emp = {}
		samples = {}
		for arm in means_true.keys():
			samples[arm] = rewards[arm] + failures[arm]
			if samples[arm] == 0:
				means_emp[arm] = 0
			else:
				means_emp[arm] = rewards[arm] / samples[arm]

		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')

	# Return the regret
	return getRegret(horizon, means_true, rewards)
