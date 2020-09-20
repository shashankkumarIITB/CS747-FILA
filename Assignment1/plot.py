import math
import matplotlib.pyplot as plt

# Create the data dictionary from the output file
# Structure of data:
# data = {
# 	'instance': {
# 		'algorithm': {
# 			'horizon': {
# 				'regret': <cummulative regret>,
# 				'numSeeds': <number of seeds>
# 			}
# 		}
# 	}
# }
def generateData(algorithms):
	data = {}
	with open('outputData.txt') as file:
		while True:
			line = file.readline()
			if not line:
				break
			else:
				instance, algorithm, seed, epsilon, horizon, regret = line.split(', ')
				if algorithm not in algorithms:
					continue
				if instance not in data.keys():
					data[instance] = {}
				data_instance = data[instance]
				if algorithm not in data_instance.keys():
					data_instance[algorithm] = {}
				data_algorithm = data_instance[algorithm]
				if horizon not in data_algorithm.keys():
					data_algorithm[horizon] = {'regret': 0, 'numSeeds': 0}
				data_horizon = data_algorithm[horizon]
				data_horizon['regret'] += float(regret)
				data_horizon['numSeeds'] += 1
	return data

# Function to generate plots based on the dictionary supplied
def generatePlots(algorithms):
	# Generate the data
	data = generateData(algorithms)
	# Plot based on the data generated
	for instance in data.keys():
		data_instance = data[instance]
		X = []
		Y = []
		for algorithm in data_instance.keys():
			data_algorithm = data_instance[algorithm]
			x = [math.log(float(horizon)) for horizon in data_algorithm.keys()]
			y = [data_algorithm[horizon]['regret'] / data_algorithm[horizon]['numSeeds'] for horizon in data_algorithm.keys()]
			X.append(x)
			Y.append(y)

		# Create a plot for this instance
		plt.ylabel(f'Regret for instace - {instance}')
		plt.xlabel('log(Horizon)')
		colors = ['c', 'r', 'y', 'k']
		algorithms = list(data_instance.keys())
		for i in range(len(X)):
			line, = plt.plot(X[i], Y[i], colors[i])
			line.set_label(f'{algorithms[i]}')
		plt.legend()
		plt.show()


if __name__ == '__main__':
	algorithms_T1 = ['epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling']
	algorithms_T2 = ['thompson-sampling', 'thompson-sampling-with-hint']
	generatePlots(algorithms_T1)
	generatePlots(algorithms_T2)
	