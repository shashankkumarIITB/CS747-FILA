# https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2020/pa-1/programming-assignment-1.html
# python3 bandit.py --instance ./instances/i-1.txt --algorithm epsilon-greedy --epsilon 0.5 --randomSeed 47 --horizon 50

import argparse
import helper
from epsilon_greedy import epsilonGreedy

# Function to parse arguments
def parseArguements(algorithms):
	parser = argparse.ArgumentParser()
	parser.add_argument('--instance', type=str, help='path to the instance file')
	parser.add_argument('--algorithm', type=str, help='algorithm choices - epsilon-greedy, ucb, kl-ucb, thompson-sampling, and thompson-sampling-with-hint')
	parser.add_argument('--randomSeed', type=helper.checkNonNegative, help='a non-negative integer to be used as seed')
	parser.add_argument('--epsilon', type=helper.checkRange, help='a number in the range [0,1]')
	parser.add_argument('--horizon', type=helper.checkNonNegative, help='a non-negative integer')
	args = parser.parse_args()
	if args.algorithm not in algorithms:
		raise AssertionError('Incorrect algorithm specified. Try using --help.')
	return args

if __name__ == '__main__':
	algorithms = ['epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling', 'thompson-sampling-with-hint']
	args = parseArguements(algorithms)
	
	# Get the true means from the file 
	means_true = helper.readFile(args.instance)

	# Call to the appropriate function
	regret = epsilonGreedy(args.randomSeed, args.horizon, means_true, args.epsilon)
	print(regret)

	