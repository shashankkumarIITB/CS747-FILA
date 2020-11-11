import matplotlib.pyplot as plt 

# Function to plot data for a single agent
def plotSingle(X, Y, title):
	plt.ylabel(f'Episodes')
	plt.xlabel('Timesteps')
	line, = plt.plot(X, Y)
	line.set_label('Sarsa(0)')
	plt.legend()
	plt.title(title)
	plt.show()

# Function to compare between different agents
def plotComparision(X, Y):
	plt.ylabel(f'Episodes')
	plt.xlabel('Timesteps')
	agents = ['Sarsa(0)', 'Q-learning', 'Expected Sarsa']
	for i in range(len(Y)):
		line, = plt.plot(X, Y[i])
		line.set_label(f'{agents[i]}')
	plt.legend()
	plt.title('Comparision between different agents')
	plt.show()
