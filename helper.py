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
