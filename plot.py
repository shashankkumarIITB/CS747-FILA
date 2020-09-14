import matplotlib

if __name__ == '__main__':
	seed_min = 50
	seed_max = 50
	data = {}
	with open('output.txt') as file:
		while True:
			line = file.readline()
			if not line:
				break
			else:
				instance, algorithm, seed, epsilon, horizon, regret = line.split(', ')
				if instance not in data.keys():
					data[instance] = {}
				data_instance = data[instance]
				if algorithm not in data_instance.keys():
					data_instance[algorithm] = {}
				data_algorithm = data_instance[algorithm]
				if horizon not in data_algorithm.keys():
					data_algorithm[horizon] = {'regret': 0, 'seeds': 0}
				data_horizon = data_algorithm[horizon]
				data_horizon['regret'] += regret
				data_horizon['seeds'] += 1

		print(data)