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

# Function to get the target value for a given time t
def getTarget(t):
	# c is the const for kl-ucb algorithm
	c = 1
	if t == 1:
		return float('inf')
	else:
		return math.log(t) + c * math.log(math.log(t))

# Function to find optimal value of q for given target and empirical mean of an arm 
def findQ(target, mean_emp, num_sample):
	q = 1
	epsilon = 10 ** -2
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
	
	# Sample arms
	for t in range(horizon):
		arm = sampleArm(means_ucbkl)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		samples[arm] += 1
		# Modify the empirical mean
		means_emp[arm] = rewards[arm] / samples[arm]
		# Find out the kl-ucb means
		target = getTarget(t+1)
		means_ucbkl = {arm: findQ(target, means_emp[arm], samples[arm]) for arm in means_true.keys()}

	if verbose:
		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')
	
	# Return the regret
	return getRegret(horizon, means_true, rewards)
