# Decode the path to be taken for the given grid

import argparse
import numpy as np
import helper

# Function to decode the path for a given grid and policy
def decoder(grid, policy):
	directions = {
		'0': 'N',
		'1': 'E',
		'2': 'S',
		'3': 'W'
	}
	path = ''
	
	row_start, col_start = np.where(grid == '3')
	row, col = row_start[0], col_start[0] 
	
	# Record the path to be taken
	while grid[row][col] != '2':
		action = policy[row][col]
		direction = directions[action]
		path += f'{direction} '
		# Decide the next row and column
		if direction == 'N':
			row -= 1
		elif direction == 'E':
			col += 1
		elif direction == 'S':
			row += 1
		elif direction == 'W':
			col -= 1

	return path


if __name__ == '__main__':
	# Parse the arguments
	parser = argparse.ArgumentParser()
	parser.add_argument("--grid", help="Path to the grid file.")
	parser.add_argument("--value_policy", help="Path to the file with the policy to be taken.")
	args = parser.parse_args()

	grid = helper.readGridFile(args.grid)
	policy = np.array(helper.readValuePolicyFile(args.value_policy)).reshape(grid.shape)
	path = decoder(grid, policy)

	if path != '':
		print(path[:-1])
