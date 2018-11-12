import random
from operator import add

from genetic_algorithm import genetic_algorithm

import pickle
distMatrix = pickle.load( open( "Matrix.p", "rb" ) )

import copy
import numpy as np

def individual():
	lst = list(range(1,len(distMatrix)))
	random.shuffle(lst)
	
	#стабильный первый элемент
	#~ pos = lst.index(50)
	#~ elt = lst.pop(pos)
	#~ lst.insert(0,elt)
	
	return lst

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
	
	
	#cost*=1000000
	A = (int(round(np.max(np.abs(app)),0))//50)*50
	cost+=(A*1000000)
	#~ cost+=np.max( np.abs( np.diff(app) )) #макс. разница длин путей
	 
	return cost

pos=1
neg=1

def comp(ind_new,ind_old):
	global pos,neg
	if fitness(ind_new)>fitness(ind_old):
		pos+=1
	else:
		neg+=1
	
	if random.randint(0,4)==0:
		print(pos/neg)
	
def mutate(individual):
	
	#random swap
	
	
	#взять элемент и вставить куда-то
	#взять последующий элемент и вставить его после вставки
	
	seed=random.randint(0,7)
	#shuffle part
	if seed==0:
		#~ individual2 = copy.deepcopy(individual)
		
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+len(individual)//2, len(individual)-1))
		
		col = individual[idx1:idx2]
		random.shuffle(col)
		individual[idx1:idx2]=col
		
		#~ comp(individual, individual2)
		
	elif seed==1:
		
		#swap
		idx1 = random.randint(0, len(individual)-1)
		idx2 = random.randint(0, len(individual)-1)
		
		tmp = individual[idx1]
		
		individual[idx1] = individual[idx2]
		individual[idx2] = tmp
		
		
		
	elif seed==2:
		
		#swap 2
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(0, len(individual)-2)
		if abs(idx2-idx1)>5:
			col1 = individual[idx1:idx1+1]
			col2 = individual[idx2:idx2+1]
			individual[idx2:idx2+1] = col1
			individual[idx1:idx1+1] = col2
		
	elif seed==3:
		
		#reverse part
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)

		col = individual[idx1:idx2]
		
		individual[idx1:idx2]=reversed(col)
		
	elif seed==4:
		
		par = copy.deepcopy(individual)
		
		#big swap
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)
		
		col = individual[idx1:idx2]
		individual[idx1:idx2] = [] #remove part
		
		idx3 = random.randint(0, len(individual))
		individual[idx3:idx3] = col
		
		
	elif seed==5:
		
		#double swap
		idx1 = random.randint(0, len(individual)-1)
		idx2 = random.randint(0, len(individual)-1)
		
		tmp = individual[idx1]
		
		individual[idx1] = individual[idx2]
		individual[idx2] = tmp
		
		idx1 = random.randint(0, len(individual)-1)
		idx2 = random.randint(0, len(individual)-1)
		
		tmp = individual[idx1]
		
		individual[idx1] = individual[idx2]
		individual[idx2] = tmp
		
	elif seed==6:
		#~ 
		#select random two, put them at selected place
		elts=[]
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
		#~ 
	elif seed==7:
		#step ahead swap
		#~ 
		idx1 = random.randint(0, len(individual)-2)
		idx2 = idx1+1
		
		col1 = individual[idx1]
		col2 = individual[idx2]
		individual[idx2] = col1
		individual[idx1] = col2
		#~ 
	
	return individual









def crossover(parent1, parent2):

	#init array
	child = [-1]*len(parent1)
	
	#fill with None
	for x in range(0,len(child)):
		child[x] = None

	start_pos = random.randint(0,len(parent1))
	end_pos = random.randint(0,len(parent1))

	if start_pos < end_pos:
		# start->end
		for x in range(start_pos,end_pos):
			child[x] = parent1[x]
	elif start_pos > end_pos:
		#end->start
		for i in range(end_pos,start_pos):
			child[i] = parent1[i]


	#replace None positions in child with remain cities
	for i in range(len(parent2)):
		if not parent2[i] in child:
			for x in range(len(child)):
				if child[x] == None:
					child[x] = parent2[i]
					break

	return child

genetic_algorithm(individual, fitness, mutate, crossover, 400, 120, 8000, 0.5)
