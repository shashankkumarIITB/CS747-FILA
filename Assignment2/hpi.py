# Implements Howard's policy iteration for MDPs

import helper
import numpy as np

# Function to return reward and probability matrix based on policy
def policyMatrix(reward, probability, policy):
	policyReward, policyProbability = [], []
	for i in range(policy.shape[0]):
		policyReward.append(reward[i][policy[i]])
		policyProbability.append(probability[i][policy[i]])
	return np.array(policyReward), np.array(policyProbability)

# Function that implements Howard's policy iteration
def hpi(numStates, numActions, startState, endStates, transitions, mdpType, discount):
	reward, probability = helper.parseTransitions(numStates, numActions, transitions)
	policy = np.array([0 for i in range(numStates)])
	policy_prev = np.ones(policy.shape)

	while not np.array_equal(policy_prev, policy):
		policy_prev = policy
		policyReward, policyProbability = policyMatrix(reward, probability, policy)

		# Iterate till the infinite norm is less than epsilon
		V, V_prev = np.zeros((1, numStates)), np.ones((1, numStates))
		epsilon = 10 ** -10
		while np.linalg.norm(V - V_prev, ord=float('inf'), axis=1) > epsilon:
			V_prev = V
			V = np.sum(policyProbability * (policyReward + discount * V), axis=1).reshape((1, numStates))
		Q = np.sum(probability * (reward + discount * V.reshape((1, 1, numStates))), axis=2)
		policy = np.argmax(Q, axis=1)

	return V, policy
