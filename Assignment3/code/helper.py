import matplotlib.pyplot as plt 

# Function to plot data
def plot(X, Y):
	plt.ylabel(f'Episodes')
	plt.xlabel('Timesteps')
	agents = ['Sarsa(0)', 'Q-learning', 'Expected Sarsa']
	colors = ['c', 'r', 'k']
	for i in range(len(Y)):
		line, = plt.plot(X, Y[i])
		line.set_label(f'{agents[i]}')
	plt.legend()
	plt.title('Comparision between different different agents')
	plt.show()
