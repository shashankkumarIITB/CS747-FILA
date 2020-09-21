# https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2020/pa-1/programming-assignment-1.html

# Time taken by each algorithm:
# 1. Epsilon-greedy ~ 4 minutes
# 2. UCB ~ 5 minutes
# 3. KL-UCB ~ 12 minutes
# 4. Thompson Sampling ~ 12 minutes
# 5. Thompson Sampling With Hint ~ 3 minutes

import argparse
import helper
from epsilon_greedy import epsilonGreedy
from ucb import ucb
from ucb_kl import ucbKL
from thompson_sampling import thompsonSampling
from thompson_sampling_with_hint import thompsonSamplingWithHint

# Function to parse arguments
def parseArguements(algorithms):
	parser = argparse.ArgumentParser()
	parser.add_argument('--instance', type=str, help='path to the instance file')
	parser.add_argument('--algorithm', default='epsilon-greedy', type=str, help='algorithm choices - epsilon-greedy, ucb, kl-ucb, thompson-sampling, and thompson-sampling-with-hint')
	parser.add_argument('--randomSeed', default=42, type=helper.checkNonNegative, help='a non-negative integer to be used as seed')
	parser.add_argument('--epsilon', default=0, type=helper.checkRange, help='a number in the range [0,1]')
	parser.add_argument('--horizon', default=10000, type=helper.checkNonNegative, help='a non-negative integer')
	parser.add_argument('--output', default='outputData', type=str, help='name of the output txt file to be created')
	parser.add_argument('--verbose', help='increase verbosity', action='store_true')
	args = parser.parse_args()
	if args.algorithm not in algorithms:
		raise AssertionError(f'Incorrect algorithm specified - "{args.algorithm}". Try using --help.')
	return args

if __name__ == '__main__':
	algorithms = ['epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling', 'thompson-sampling-with-hint']
	args = parseArguements(algorithms)
	
	# Get the true means from the file 
	means_true = helper.readFile(args.instance)

	# Call to the appropriate function
	regret = None
	if args.algorithm == 'epsilon-greedy':
		regret = epsilonGreedy(args.randomSeed, args.horizon, means_true, args.epsilon, args.verbose)
	elif args.algorithm == 'ucb':
		regret = ucb(args.randomSeed, args.horizon, means_true, args.verbose)
	elif args.algorithm == 'kl-ucb':
		regret = ucbKL(args.randomSeed, args.horizon, means_true, args.verbose)
	elif args.algorithm == 'thompson-sampling':
		regret = thompsonSampling(args.randomSeed, args.horizon, means_true, args.verbose)
	elif args.algorithm == 'thompson-sampling-with-hint':
		regret = thompsonSamplingWithHint(args.randomSeed, args.horizon, means_true, args.verbose)
	else:
		regret = float('inf')
	
	if regret is not None:
		# Print output to console and write to file
		result = f'{args.instance}, {args.algorithm}, {args.randomSeed}, {args.epsilon}, {args.horizon}, {regret}'
		print(result)
		helper.writeFile(f'{args.output}.txt', result)
