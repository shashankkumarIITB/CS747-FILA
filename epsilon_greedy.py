# python3 bandit.py --instance ./instances/i-2.txt --algorithm epsilon-greedy --randomSeed 42 --epsilon 0.3 --verbose --horizon 100000

import operator, random
from helper import getReward, getRegret

# Returns the modified rewards afer sampling an arm
def sampleArm(means_emp, epsilon):
	arm_max = max(means_emp.items(), key=operator.itemgetter(1))[0]
	toss = random.random()
	if toss <= 1 - epsilon:
		# Exploit based on empirical mean
		return arm_max
	else:
		# Explore
		return random.randint(1, len(means_emp))

# Function for epsilon-greedy sampling algorithm
def epsilonGreedy(seed, horizon, means_true, epsilon, verbose=False):
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	samples = {i: 0 for i in means_true.keys()}
	means_emp = {i: 0.0 for i in means_true.keys()}

	# Sample bandit-arms
	for _ in range(horizon):
		arm = sampleArm(means_emp, epsilon)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		samples[arm] += 1
		means_emp[arm] = rewards[arm] / samples[arm]

	if verbose:
		print(f'True means:\n{means_true}')
		print(f'Empirical means:\n{means_emp}')
		print(f'Number of pulls:\n{samples}')

	# Return the regret
	return getRegret(horizon, means_true, rewards)
