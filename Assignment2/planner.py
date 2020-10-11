# https://www.cse.iitb.ac.in/~shivaram/teaching/cs747-a2020/pa-2/programming-assignment-2.html

import argparse
import numpy as np
import helper

# Convert the transitions to numpy arrays
def parseTransitions(numStates, numActions, transitions):
	reward = np.zeros((numStates, numActions, numStates))
	probability = np.zeros((numStates, numActions, numStates))
	for transition in transitions:
		s1, ac, s2, r, p = transition
		s1, ac, s2 = int(s1), int(ac), int(s2)
		reward[s1][ac][s2] = r
		probability[s1][ac][s2] = p
	return reward, probability

# Function to implement value iteration to find optimal policy
def vi(numStates, numActions, startState, endStates, transitions, mdpType, discount):
	reward, probability = parseTransitions(numStates, numActions, transitions)
	Q, V = np.zeros((numStates, numActions)), np.zeros((1, 1, numStates))
	V_prev = np.ones(V.shape)

	# Iterate till the infinite norm is less than 
	epsilon = 10 ** -6
	while np.linalg.norm(V - V_prev, ord=float('inf'), axis=2) > epsilon:
		V_prev = V
		Q = np.sum(probability * (reward + discount * V), axis=2)
		V = np.max(Q, axis=1).reshape((1, 1, numStates))
	return V

# Parse the arguments
parser = argparse.ArgumentParser()
parser.add_argument("--mdp", help="Path to the mdp file.")
parser.add_argument("--algorithm", help="Algorithm to calculate optimal value and policy.")
args = parser.parse_args()

# Read the mdp file
numStates, numActions, startState, endStates, transitions, mdpType, discount = helper.parseFile(args.mdp)

# Call to the function
print(f'Number of states: {numStates}')
print(f'Number of actions: {numActions}')
V = vi(numStates, numActions, startState, endStates, transitions, mdpType, discount)
print(V)

