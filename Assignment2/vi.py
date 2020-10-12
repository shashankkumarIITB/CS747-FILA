# Implements value iteration for MDPs

import helper
import numpy as np

# Function to implement value iteration to find optimal policy
def vi(numStates, numActions, startState, endStates, transitions, mdpType, discount):
	reward, probability = helper.parseTransitions(numStates, numActions, transitions)
	Q, V = np.zeros((numStates, numActions)), np.zeros((1, 1, numStates))
	V_prev = np.ones(V.shape)

	# Iterate till the infinite norm is less than epsilon
	epsilon = 10 ** -6
	while np.linalg.norm(V - V_prev, ord=float('inf'), axis=2) > epsilon:
		V_prev = V
		Q = np.sum(probability * (reward + discount * V), axis=2)
		V = np.max(Q, axis=1).reshape((1, 1, numStates))

	# Calculate the optimal policy
	policy = np.argmax(Q, axis=1)
	return V, policy

