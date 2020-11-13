import matplotlib.pyplot as plt 

# Function to plot data for a single agent
def plotSingle(X, Y, title):
	plt.ylabel(f'Episodes')
	plt.xlabel('Timesteps')
	line, = plt.plot(X, Y)
	line.set_label(title)
	plt.legend()
	plt.title(title)
	plt.show()

# Function to compare between different agents
def plotComparision(X, Y, role):
	plt.ylabel(f'Episodes')
	plt.xlabel('Timesteps')
	if role == '1':
		agents = ['Sarsa(0)', 'Q-learning', 'Expected Sarsa']
		title = 'Comparision between different agents'
	elif role == '2':
		agents = ['Sarsa(0)', 'With King\'s move', 'With King\'s move and stochastic wind']
		title = 'Comparision for different scenarios'
	for i in range(len(Y)):
		line, = plt.plot(X, Y[i])
		line.set_label(f'{agents[i]}')
	plt.legend()
	plt.title(title)
	plt.show()
