# https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2020/pa-2/programming-assignment-2.html

import argparse
import helper
from vi import vi
from hpi import hpi
from lp import lp

if __name__ == '__main__':
	# Parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--mdp", help="Path to the mdp file.")
	parser.add_argument("--algorithm", help="Algorithm - vi, hpi or lp - to calculate optimal value and policy.")
	args = parser.parse_args()

	# Read the mdp file
	numStates, numActions, startState, endStates, transitions, mdpType, discount = helper.parseFile(args.mdp)

	print(f'Number of states: {numStates}')
	print(f'Number of actions: {numActions}')

	V, policy = None, None

	# Call to the respective function
	if args.algorithm == 'vi':
		V, policy = vi(numStates, numActions, startState, endStates, transitions, mdpType, discount)
	elif args.algorithm == 'hpi':
		V, policy = hpi(numStates, numActions, startState, endStates, transitions, mdpType, discount)
	elif args.algorithm == 'lp':
		V, policy = lp(numStates, numActions, startState, endStates, transitions, mdpType, discount)
	else:
		raise ValueError(f'Illegal arguments specified for algorithm - {args.algorithm}')

	helper.printOutput(V, policy)
