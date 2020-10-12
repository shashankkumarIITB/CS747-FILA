# Function to solve MDP based on Linear Programming

import helper
import numpy as np
from pulp import *

def lp(numStates, numActions, startState, endStates, transitions, mdpType, discount):
	reward, probability = helper.parseTransitions(numStates, numActions, transitions)

	# Create the problem instance
	problem = LpProblem('MDP', LpMaximize)
	
	# Create the LP variables
	V = []
	for i in range(numStates):
		V.append(LpVariable(f'V{i}'))

	# Add the objective function
	problem += lpSum([-v for v in V]), 'Value function to maximize'

	# Add the constraints
	value = np.sum(probability * reward, axis=2)
	for s1 in range(numStates):
		for ac in range(numActions):
			problem += V[s1] - lpSum([probability[s1][ac][s2] * discount * V[s2] for s2 in range(numStates)]) >= value[s1][ac], f'State: {s1}, Action: {ac}'

	# Solve the problem
	problem.solve(PULP_CBC_CMD(msg=0))

	V = np.array([v.varValue for v in problem.variables()]).reshape((1, 1, numStates))
	Q = np.sum(probability * (reward + discount * V), axis=2)
	policy = np.argmax(Q, axis=1)
	return V, policy