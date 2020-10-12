# Functions to encode the maze as an MDP

import argparse
import numpy as np
import helper

# Function to return the state based on position in the grid
def getState(rows, i, j):
	return (i - 1) * rows + (j - 1)

# Function to return reward based on the state encountered
def getReward(state):
	if state == '2':
		return 100
	return -1

# Function to return probability of transition based on the state encountered
def getProbability(state):
	if state == '1':
		return 0
	return 1

# Encode the grid in the form of transitions
def encode(grid):
	# MDP parameters
	rows, cols = grid.shape
	numStates = rows * cols
	actions = {
		'N': 0,
		'E': 1,
		'S': 2,
		'W': 3
	}
	numActions = len(actions)
	startState, endStates = None, []
	transitions = []
	mdptype = 'continuing'
	discount = 1

	# Pad the grid
	grid = np.pad(grid, 1, constant_values=(1))

	for i in range(1, rows+1):
		for j in range(1, cols+1):
			if grid[i][j] != '1':
				current_state = getState(rows, i, j)
				# Check if the state is a start or end state
				if grid[i][j] == '3':
					startState = current_state
				elif grid[i][j] == '2':
					endStates.append(current_state)
					# No transitions from the end state
					continue
				
				# Add the transitions
				# 1. North
				next_state = getState(rows, i-1, j)
				state_value = grid[i-1, j]
				transitions.append((current_state, actions['N'], next_state, getReward(state_value), getProbability(state_value)))
				# 2. East
				next_state = getState(rows, i, j+1)
				state_value = grid[i, j+1]
				transitions.append((current_state, actions['E'], next_state, getReward(state_value), getProbability(state_value)))
				# 3. South
				next_state = getState(rows, i+1, j)
				state_value = grid[i+1, j]
				transitions.append((current_state, actions['S'], next_state, getReward(state_value), getProbability(state_value)))
				# 4. West
				next_state = getState(rows, i, j-1)
				state_value = grid[i, j-1]
				transitions.append((current_state, actions['W'], next_state, getReward(state_value), getProbability(state_value)))

	helper.printMdp(numStates, numActions, startState, endStates, transitions, mdptype, discount)


if __name__ == '__main__':
	# Parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--grid", help="Path to the grid file.")
	args = parser.parse_args()

	grid = helper.readGridFile(args.grid)
	encode(grid)