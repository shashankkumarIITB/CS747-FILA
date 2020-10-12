# File with the helper functions

import os
import numpy as np

# Function to check if the file exists
def checkFileExists(path):
	if not os.path.exists(path):
		raise FileNotFoundError(f'File not found at the path - {path}')

# Read and parse the mdp file
def parseMdpFile(path):
	checkFileExists(path)
	with open(path) as file:
		numStates = file.readline().split('\n')[0].split(' ')[1]
		numActions = file.readline().split('\n')[0].split(' ')[1]
		startState = file.readline().split('\n')[0].split(' ')[1]
		endStates = [int(e) for e in file.readline().split('\n')[0].split(' ')[1:]]
		transitions = []
		line = file.readline().split('\n')[0].split(' ')
		while (line[0] == 'transition'):
			transition = [float(e) for e in line[1:]]
			transitions.append(transition)
			line = file.readline().split('\n')[0].split(' ')
		mdptype = line[1]
		discount = file.readline().split('\n')[0].split(' ')[1]
	return int(numStates), int(numActions), int(startState), endStates, transitions, mdptype, float(discount)

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

# Function to print output to terminal
def printOutput(V, policy):
	V = V.reshape((-1))
	policy = policy.reshape((-1))
	for i in range(V.shape[0]):
		print(f'{V[i]:.6f} {policy[i]}')

# Read and parse the maze file
def parseGridFile(path):
	checkFileExists(path)
	grid = []
	with open(path) as file:
		line = file.readline()
		while line:
			row = line.split('\n')[0].split(' ')
			grid.append(row)
			line = file.readline()
	return np.array(grid)

# Print MDP generated from grid to output
def printMdp(numStates, numActions, startState, endStates, transitions, mdptype, discount):
	print(f'numStates {numStates}')
	print(f'numActions {numActions}')
	print(f'start {startState}')

	if len(endStates) == 0:
		print(f'endStates -1')
	else:	
		endString = '' 
		for e in endStates:
			endString += f'{e}'
		print(f'end {endString[:-1]}')

	for transition in transitions:
		s1, ac, s2, r, p = transition
		print(f'transition {s1} {ac} {s2} {r} {p}')

	print(f'mdptype {mdptype}')
	print(f'discount {discount}')