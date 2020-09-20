# python3 bandit.py --instance ./instances/i-2.txt --algorithm thompson-sampling-with-hint--randomSeed 42 --verbose --horizon 100000

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

# Returns an arm which is within epsilon of the maximum true mean
def epsilonClose(means_true_max, means_emp):
	epsilon = 0.05
	for arm in means_emp.keys():
		if abs(means_true_max - means_emp[arm]) < epsilon:
			return arm
	return -1

# Function for epsilon-greedy sampling algorithm
def thompsonSamplingWithHint(seed, horizon, means_true, verbose=False):
	np.random.seed(seed)
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	failures = {i: 0 for i in means_true.keys()}
	samples = {i: 0 for i in means_true.keys()}
	means_emp = {i: 0 for i in means_true.keys()}

	# Compute the maximum value amongst the true means
	means_true_max = max(means_true.values())

	# Sample bandit-arms
	for _ in range(horizon):
		arm = epsilonClose(means_true_max, means_emp)
		if arm == -1:
			arm = sampleArm(rewards, failures)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		failures[arm] += 1 - reward
		samples[arm] += 1
		means_emp[arm] = rewards[arm] / samples[arm]

	if verbose:
		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')

	# Return the regret
	return getRegret(horizon, means_true, rewards)
