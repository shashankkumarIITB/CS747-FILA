import numpy as np

# Class to implement gridworld problem
class Gridworld:

	# Initialize the world
	def __init__(self, rows=7, cols=10, start=(3, 0), end=(3, 7), seed=0, stochastic=False):
		self.rows = 7
		self.cols = 10
		# Start and end state
		self.start = start[0] * self.cols + start[1]
		self.end = end[0] * self.cols + end[1]
		# Wind in the grid
		self.wind = self.generateWind()
		self.stochastic = stochastic
		self.actions = {
			0: 'N', 
			1: 'E', 
			2: 'S', 
			3: 'W', 
			4: 'NE',
			5: 'SE',
			6: 'SW',
			7: 'NW',
		}
		# Random number generator
		self.rg = np.random.default_rng(seed=seed)

	# Function to generate wind in every column
	def generateWind(self):
		return [0, 0, 0, 1, 1, 1, 2, 2, 1, 0]

	# Function to return wind magnitude at a given column
	def getWind(self, col):
		if self.stochastic:
			return self.wind[col] + self.rg.integers(-1, 2) 
		else:
			return self.wind[col]

	# Return the next state based on the current state and action taken
	def nextState(self, state, action):
		row, col = state // self.cols, state % self.cols
		wind = self.getWind(col)
		action = self.actions[action]
		if action == 'N': 
			row, col = row - wind - 1, col
		elif action == 'NE':
			row, col = row - wind - 1, col + 1
		elif action == 'E':
			row, col = row - wind, col + 1
		elif action == 'SE':
			row, col = row - wind + 1, col + 1
		elif action == 'S':
			row, col = row - wind + 1, col
		elif action == 'SW':
			row, col = row - wind + 1, col - 1
		elif action == 'W':
			row, col = row - wind, col - 1
		elif action == 'NW':
			row, col = row - wind - 1, col - 1

		# Wind does not work on the edges of the grid
		if row < 0: 
			row = 0
		elif row >= self.rows:
			row = self.rows - 1

		if col < 0:
			col = 0
		elif col >= self.cols:
			col = self.cols - 1

		return row * self.cols + col

	# Return the reward based on the next state 
	def getReward(self, next_state):
		if next_state == self.end:
			return 100
		else :
			return -1