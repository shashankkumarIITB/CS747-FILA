import operator, random

# Raises an exception if a negative number is provided as argument
def checkNonNegative(number):
	try:
		integer = int(number)
		if integer < 0:
			raise AssertionError('Value must be non-negative.')
		return integer
	except Exception as e:
		raise e

# Raise exception if number is not in range [0,1]
def checkRange(number):
	try:
		number = float(number)
		if number > 1 or number < 0:
			raise AssertionError('Value must be in the range [0,1] (both inclusive).')
		return number
	except Exception as e:
		raise e

# Return true if 
# Read and return true mean values from the filepath specfied
def readFile(path):
	with open(path, 'r') as file:
		means = {}
		i = 1
		while True:
			line = file.readline()
			if not line:
				break
			try:
				mean = float(line)
				means[i] = mean
				i += 1
			except Exception as e:
				raise e
		return means

# Write output to file
def writeFile(path, string):
	with open(path, 'a+') as file:
		file.write(f'{string}\n')

# Remove the last newline from the file
def removeNewline(path):
	lines = []
	# Read all the data
	with open(path, 'r') as file:
		lines = file.readlines()

	# Write the lines after stripping the last newline character
	lines[-1] = lines[-1].split('\n')[0]
	with open(path, 'w') as file:
		for line in lines:
			file.write(line)


# Function to get reward based on the arm sampled
def getReward(arm_probability):
	toss = random.random()
	if toss < arm_probability:
		return 1
	else:
		return 0

# Function to return regret given true means and rewards
def getRegret(horizon, means_true, rewards):
	p_star = max(means_true.items(), key=operator.itemgetter(1))[1]
	regret = horizon * p_star - sum(rewards.values())
	return regret