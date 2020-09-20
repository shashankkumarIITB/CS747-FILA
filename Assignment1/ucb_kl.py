# python3 bandit.py --instance ./instances/i-2.txt --algorithm kl-ucb --randomSeed 42 --verbose --horizon 10000

import math, operator, random
from helper import getReward, getRegret

# Function to return KL divergence of two numbers p and q
def kl(p, q):
	if p == 0 or p == 1:
		return 0
	elif q == 0 or q ==1:
		return float('inf')
	else:
		return p * math.log(p / q) + (1 - p) * math.log((1 - p) / (1 - q))

# Function to find optimal value of q given horizon and empirical mean of an arm 
def findQ(horizon, target, mean_emp, num_sample):
	q = 1
	epsilon = 10 ** -1
	value = kl(mean_emp, q) * num_sample
	while q >= mean_emp and value > target:
		q -= epsilon
		value = kl(mean_emp, q) * num_sample
	return q

# Returns the modified rewards afer sampling an arm
def sampleArm(means_ucbkl):
	arm_max = max(means_ucbkl.items(), key=operator.itemgetter(1))[0]
	return arm_max

# Function for kl-ucb sampling algorithm
def ucbKL(seed, horizon, means_true, verbose=False):
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	samples = {i: 0 for i in means_true.keys()}
	means_emp = {i: 0 for i in means_true.keys()}
	means_ucbkl = {i: float('inf') for i in means_true.keys()}
	
	# c is the const for kl-ucb algorithm
	c = 3
	target = math.log(horizon) + c * math.log(math.log(horizon))
	
	# Sample arms
	for _ in range(horizon):
		arm = sampleArm(means_ucbkl)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		samples[arm] += 1
		means_emp[arm] = rewards[arm] / samples[arm]
		means_ucbkl[arm] = findQ(horizon, target, means_emp[arm], samples[arm])

	if verbose:
		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')
	
	# Return the regret
	return getRegret(horizon, means_true, rewards)
