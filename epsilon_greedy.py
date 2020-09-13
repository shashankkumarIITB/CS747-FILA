import operator, random

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

# Function to get reward based on the arm sampled
def getReward(arm_prob):
	toss = random.random()
	if toss < arm_prob:
		return 1
	else:
		return 0

# Function for epsilon-greedy strategy
def epsilonGreedy(seed, horizon, means_true, epsilon):
	random.seed(seed)
	rewards = {i: 0 for i in means_true.keys()}
	samples = {i: 0 for i in means_true.keys()}
	means_emp = {i: 0.0 for i in means_true.keys()}

	# Sample bandit-arms
	for t in range(horizon):
		arm = sampleArm(means_emp, epsilon)
		reward = getReward(means_true[arm])
		rewards[arm] += reward
		samples[arm] += 1
		means_emp[arm] = rewards[arm] / samples[arm]

	# Return the regret
	p_star = max(means_true.items(), key=operator.itemgetter(1))[1]
	regret = horizon * p_star - sum(rewards.values())
	return regret