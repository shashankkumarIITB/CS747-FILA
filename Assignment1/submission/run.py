import os

# Function to run for T1 and T2
def run(algorithms, epsilon, horizons, instances, filename): 
	for algorithm in algorithms:
		for instance in instances:
			for horizon in horizons:
				for seed in range(0, 50):
					os.system(f'python3 bandit.py --instance {instance} --algorithm {algorithm} --randomSeed {seed} --epsilon {epsilon} --horizon {horizon} --output {filename}')

if __name__ == '__main__':
	algorithms_T1 = ['epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling']
	# algorithms_T2 = ['thompson-sampling', 'thompson-sampling-with-hint']
	algorithms_T2 = ['thompson-sampling-with-hint']
	epsilon = 0.02
	horizons = [100, 400, 1600, 6400, 25600, 102400]
	dir_insances = './instances'
	instances = [f'{dir_insances}/i-1.txt', f'{dir_insances}/i-2.txt', f'{dir_insances}/i-3.txt']

	# run(algorithms_T1, epsilon, horizons, instances, 'outputDataT1')
	run(algorithms_T2, epsilon, horizons, instances, 'outputDataT2')
