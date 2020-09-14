import os

if __name__ == '__main__':
	algorithms = ['epsilon-greedy', 'ucb', 'kl-ucb', 'thompson-sampling']
	epsilon = 0.02
	horizons = [100, 400, 6400, 25600, 102400]
	dir_insances = './instances'
	instances = [f'{dir_insances}/i-1.txt', f'{dir_insances}/i-2.txt', f'{dir_insances}/i-3.txt']

	for i in range(len(algorithms)):
		for instance in instances:
			for horizon in horizons:
				for seed in range(0, 50):
					os.system(f'python3 bandit.py --instance {instance} --algorithm {algorithms[i]} --randomSeed {seed} --epsilon {epsilon} --horizon {horizon}')
