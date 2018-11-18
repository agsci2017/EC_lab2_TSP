import pandas as pd
import numpy as np
import random
import pickle
import networkx as nx
G = nx.Graph()

dt=pd.read_csv('xqf131.tsp')
import matplotlib.pyplot as plt

way = [8, 2, 3, 9, 10, 4, 11, 23, 38, 39, 40, 41, 42, 24, 43, 44, 61, 60, 59, 73, 72, 80, 86, 85, 84, 83, 79, 76, 71, 70, 66, 67, 63, 58, 57, 56, 62, 65, 69, 75, 64, 68, 77, 78, 81, 82, 87, 88, 92, 94, 90, 91, 95, 96, 97, 104, 103, 111, 110, 109, 115, 119, 116, 120, 117, 122, 129, 128, 127, 131, 126, 125, 124, 106, 107, 113, 108, 99, 102, 101, 100, 105, 114, 118, 121, 130, 123, 112, 98, 93, 89, 74, 53, 45, 46, 54, 55, 47, 48, 49, 50, 51, 52, 36, 37, 22, 35, 34, 21, 33, 32, 31, 30, 20, 29, 28, 27, 26, 19, 25, 17, 16, 15, 14, 18, 13, 5, 12, 6, 1, 7] #582. (best=564)
#~ way = [55, 64, 68, 75, 77, 78, 81, 82, 87, 88, 92, 94, 99, 90, 91, 95, 96, 97, 104, 103, 111, 110, 109, 115, 119, 116, 120, 117, 122, 129, 128, 127, 131, 126, 125, 124, 113, 108, 107, 106, 102, 101, 100, 105, 114, 118, 121, 130, 123, 112, 98, 93, 89, 74, 53, 45, 26, 27, 28, 19, 25, 17, 16, 15, 14, 18, 13, 5, 12, 6, 1, 7, 8, 2, 3, 9, 10, 4, 11, 24, 44, 43, 42, 41, 40, 23, 38, 39, 59, 60, 61, 73, 72, 80, 86, 85, 84, 83, 79, 76, 71, 67, 63, 66, 70, 69, 65, 62, 56, 57, 58, 52, 51, 50, 49, 48, 47, 33, 34, 35, 36, 37, 22, 21, 32, 31, 20, 30, 29, 46, 54] #585. (best=564)


import pickle
distMatrix = pickle.load( open( "Matrix.p", "rb" ) )

def fitness(individual):
	#sum
	cost = 0
	
	for i in range(0, len(individual)-1):
		cost += distMatrix[individual[i]][individual[i+1]]
	cost += distMatrix[individual[-1]][individual[0]]
	
	#вторичный критерий отбора
	#в множестве равновесных решений, преимущество будет у решения с наименьшей максимальной разницей длин путей
	#~ app=[]
	#~ for i in range(0, len(individual)-1):
		#~ app.append( distMatrix[individual[i]][individual[i+1]] )
	#~ app.append( distMatrix[-1][individual[0]] )
	
	
	#~ cost*=100000000
	#~ cost+=np.max( np.abs(np.diff(app) )) #макс. разница длин путей
	 
	return cost/1000.0


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
