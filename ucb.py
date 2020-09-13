# python3 bandit.py --instance ./instances/i-2.txt --algorithm ucb --randomSeed 47 --verbose --horizon 10000

import math, operator, random
from helper import getReward, getRegret

# Returns the modified rewards afer sampling an arm
def sampleArm(means_ucb):
	arm_max = max(means_ucb.items(), key=operator.itemgetter(1))[0]
	return arm_max

# Extra term to be added to means_emp
def extraTerm(t, numSamples):
	return math.sqrt(2 * math.log(t) / numSamples)

# Function for ucb sampling algorithm
def ucb(seed, horizon, means_true, verbose=False):
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	samples = {i: 0 for i in means_true.keys()}
	means_emp = {i: 0 for i in means_true.keys()}
	means_ucb = {i: float('inf') for i in means_true.keys()}
	
	# Sample arms
	for t in range(horizon):
		arm = sampleArm(means_ucb)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		samples[arm] += 1
		means_emp[arm] = rewards[arm] / samples[arm]
		means_ucb[arm] = means_emp[arm] + extraTerm(t+1, samples[arm])

	if verbose:
		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')
	
	# Return the regret
	return getRegret(horizon, means_true, rewards)
