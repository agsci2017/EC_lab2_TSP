import pandas as pd
import numpy as np
import random
import pickle
import networkx as nx
G = nx.Graph()

dt=pd.read_csv('xqf131.tsp')
import matplotlib.pyplot as plt

way = [11, 4, 10, 9, 3, 2, 8, 7, 1, 6, 12, 5, 13, 18, 14, 15, 16, 17, 25, 26, 27, 19, 20, 21, 22, 23, 24, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 46, 45, 53, 74, 68, 64, 54, 55, 47, 48, 49, 50, 51, 52, 57, 56, 62, 65, 69, 66, 70, 76, 71, 67, 63, 58, 59, 60, 61, 73, 72, 80, 79, 83, 84, 85, 86, 90, 91, 95, 96, 97, 104, 103, 111, 110, 99, 94, 92, 88, 87, 82, 81, 78, 75, 77, 89, 93, 98, 100, 105, 101, 102, 106, 107, 113, 108, 109, 115, 119, 116, 120, 117, 122, 129, 128, 127, 126, 125, 124, 121, 118, 114, 112, 123, 130, 131] #560. (best=564)



import pickle
distMatrix = pickle.load( open( "Matrix.p", "rb" ) )

def fitness(individual):
	#sum
	cost = 0
	
	for i in range(0, len(individual)-1):
		cost += distMatrix[individual[i]][individual[i+1]]
	cost += distMatrix[len(individual)-1][0]
	
	#вторичный критерий отбора
	#в множестве равновесных решений, преимущество будет у решения с наименьшей максимальной разницей длин путей
	app=[]
	for i in range(0, len(individual)-1):
		app.append( distMatrix[individual[i]][individual[i+1]] )
	app.append( distMatrix[-1][individual[0]] )
	
	
	cost*=100000000
	cost+=np.max( np.abs(np.diff(app) )) #макс. разница длин путей
	 
	return cost


plt.title(fitness(way))

plt.scatter(dt['x'].values, dt['y'].values)

xes = []
yes = []

way.append(way[0])
for i in way:
	print(i)
	xes.append(dt.loc[(dt['idx']==i)]['x'].values[0])
	yes.append(dt.loc[(dt['idx']==i)]['y'].values[0])

print(xes)
print(yes)


plt.plot(xes,yes)
plt.show()
