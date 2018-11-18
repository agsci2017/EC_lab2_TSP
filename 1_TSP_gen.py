import pandas as pd
import numpy as np
import random
import pickle
import networkx as nx
G = nx.Graph()

dt=pd.read_csv('xqf131.tsp')



ncities=len(dt['idx'].values)
cities=dt['idx'].values

Matrix = [[0 for x in range(0,ncities+1)] for y in range(0,ncities+1)]

import math
for i in cities:
	print(i)
	X1 = float(dt.loc[(dt['idx']==i)]['x'])
	Y1 = float(dt.loc[(dt['idx']==i)]['y'])
	
	for j in cities:	
		X2 = float(dt.loc[(dt['idx']==j)]['x'])
		Y2 = float(dt.loc[(dt['idx']==j)]['y'])
		
		#print(X1,X2,Y1,Y2)
		dist = math.sqrt((X2-X1)*(X2-X1) + (Y2-Y1)*(Y2-Y1))
		#~ print(dist)
		Matrix[i][j]=int(round(dist*1000,3)) #плавающая точка может давать погрешности на арифметических операциях(+),
		#вызывая некорректные сравнения 350.00000000 != 350.00000000

print(Matrix[0])
print(Matrix[-1])
pickle.dump( Matrix, open( "Matrix.p", "wb" ) )

import sys
sys.exit(0)
