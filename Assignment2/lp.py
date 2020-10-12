# Function to solve MDP based on Linear Programming

import helper
import numpy as numpy
from pulp import *

def lp(numStates, numActions, startState, endStates, transitions, mdpType, discount):
	# Create the problem instance
	problem = LpProblem('MDP', LpMaximize)
	
	# Create the LP variables
	V = []
	for i in range(numStates):
		V.append(LpVariable(f'V{i}'))

	# Add the objective function
	problem += lpSum([-v for v in V]), 'Value function to maximize'