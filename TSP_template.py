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
	cost += distMatrix[individual[-1]][individual[0]]
	
	#вторичный критерий отбора
	#в множестве равновесных решений, преимущество будет у решения с наименьшей максимальной разницей длин путей
	#~ app=[]
	#~ for i in range(0, len(individual)-1):
		#~ app.append( distMatrix[individual[i]][individual[i+1]] )
	#~ app.append( distMatrix[-1][individual[0]] )
	
	
	#~ #cost*=1000000
	#~ A = (int(round(np.max(np.abs(app)),0))//50)*50
	#~ cost+=(A*1000000)
	#~ cost+=np.max( np.abs( np.diff(app) )) #макс. разница длин путей
	 
	return cost

pos={}
neg={}

CNT=0

#~ fstat=open("stat.csv","w")

KEYS=[]

def comp(ind_new,ind_old,nam):
	return
	
	global pos,neg,CNT,KEYS
	
	if not nam in pos.keys():
		pos[nam]=1
		neg[nam]=1
	
	if fitness(ind_old)>fitness(ind_new):
		#~ pos[nam]+=(fitness(ind_old)-fitness(ind_new)) #positive change in fitness
		pos[nam]+=1 #positive change in fitness
	else:
		#~ neg[nam]+=(fitness(ind_new)-fitness(ind_old))
		neg[nam]+=1
	
	if CNT==1000:
		KEYS=list(pos.keys())
		for k in KEYS:
			fstat.write(k+",")
		fstat.write("\n")
	
	if CNT%1000==0 and CNT>1000:
		for k in KEYS:
			#~ print(k," : ", pos[k]/neg[k])
			fstat.write(str(pos[k]/neg[k])+",")
			#fstat.write(str(neg[k])+",")
			pos[k]=1
			neg[k]=1
		fstat.write("\n")
		fstat.flush()
	CNT+=1

def RR(a):
	idx1=0
	idx2=0
	
	while idx1==idx2:
		idx1 = random.randint(0,len(a))
		idx2 = random.randint(0,len(a))
	
	if idx1>idx2:
		#~ print(idx1,idx2)
		#~ print(a+a)
		part1 = (a+a)[:idx1]
		part2 = (a+a)[idx1:idx2+len(a)]
		part3 = (a+a)[idx2+len(a):]
		#~ print(part1,part2,part3)
		#~ print(len(part1),len(part2),len(part3))
		
		part2=list(reversed(part2))
		#~ print(part1,part2,part3)
		#~ print(len(part1),len(part2),len(part3))
		
		#~ print("a:     ",a)
		partA = (part1+part2)[:len(a)]
		#~ print("partA: ",partA)
		partB = (part1+part2)[len(a):]
		#~ print("partB: ",partB)
		partA[:len(partB)]=partB
		#~ print("newA:  ",partA)
		a=partA
	
	if idx1<idx2:
		col = a[idx1:idx2]
		col=list(reversed(col))
		a[idx1:idx2]=col
	
	return copy.deepcopy(a)

#full shuffle
def RS(a):
	idx1=0
	idx2=0
	
	while idx1==idx2 or abs(idx1-idx2)>15:
		idx1 = random.randint(0,len(a))
		idx2 = random.randint(0,len(a))
	
	if idx1>idx2:
		#~ print(idx1,idx2)
		#~ print(a+a)
		part1 = (a+a)[:idx1]
		part2 = (a+a)[idx1:idx2+len(a)]
		part3 = (a+a)[idx2+len(a):]
		#~ print(part1,part2,part3)
		#~ print(len(part1),len(part2),len(part3))
		
		#~ part2=list(reversed(part2))
		random.shuffle(part2)
		#~ print(part1,part2,part3)
		#~ print(len(part1),len(part2),len(part3))
		
		#~ print("a:     ",a)
		partA = (part1+part2)[:len(a)]
		#~ print("partA: ",partA)
		partB = (part1+part2)[len(a):]
		#~ print("partB: ",partB)
		partA[:len(partB)]=partB
		#~ print("newA:  ",partA)
		a=partA
	
	if idx1<idx2:
		col = a[idx1:idx2]
		random.shuffle(col)
		a[idx1:idx2]=col
	
	return copy.deepcopy(a)

def mutate(individual):
	
	basis = copy.deepcopy(individual)
	
	
	#~ seed=random.choice([SEED1,SEED2])
	seed=random.choice([17,7,SEED1])
	seed=random.choice([SEED1])
	
	#shuffle part
	if seed==15:
		
		individual=RR(individual)

	if seed==16:
		
		individual=RS(individual)
		
	if seed==0:
		
		
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+len(individual)//2, len(individual)-1))
		
		col = individual[idx1:idx2]
		random.shuffle(col)
		individual[idx1:idx2]=col
		
		comp(individual, basis,"shuffle len<half")
		
	if seed==9:
		
		
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)
		
		col = individual[idx1:idx2]
		random.shuffle(col)
		individual[idx1:idx2]=col
		
		comp(individual, basis,"shuffle len<max")
		
	elif seed==1:
		
		#swap
		idx1 = random.randint(0, len(individual)-1)
		idx2 = random.randint(0, len(individual)-1)
		
		tmp = individual[idx1]
		
		individual[idx1] = individual[idx2]
		individual[idx2] = tmp
		
		comp(individual, basis,"swap")
		
	elif seed==2:
		
		#swap 2
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(0, len(individual)-2)
		if abs(idx2-idx1)>5:
			col1 = individual[idx1:idx1+1]
			col2 = individual[idx2:idx2+1]
			individual[idx2:idx2+1] = col1
			individual[idx1:idx1+1] = col2
		
		comp(individual, basis,"swap2")
		
	elif seed==3:
		
		#reverse part
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)

		col = individual[idx1:idx2]
		
		individual[idx1:idx2]=reversed(col)
		
		comp(individual, basis,"reverse part")
	elif seed==13:
		
		#reverse part
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+15, len(individual)-1))

		col = individual[idx1:idx2]
		
		individual[idx1:idx2]=reversed(col)
		
		comp(individual, basis,"reverse part<15")
		
	elif seed==4:
		
		par = copy.deepcopy(individual)
		
		#big swap
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)
		
		col = individual[idx1:idx2]
		individual[idx1:idx2] = [] #remove part
		
		idx3 = random.randint(0, len(individual))
		individual[idx3:idx3] = col
		
		comp(individual, basis,"eject-insert part")
		
	elif seed==8:
		
		par = copy.deepcopy(individual)
		
		#big swap
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+30, len(individual)-1))
		
		col = individual[idx1:idx2]
		individual[idx1:idx2] = [] #remove part
		
		idx3 = random.randint(0, len(individual))
		individual[idx3:idx3] = col
		
		comp(individual, basis,"eject-insert part with len<30")
		
	elif seed==10:
		
		par = copy.deepcopy(individual)
		
		#big swap
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+15, len(individual)-1))
		
		col = individual[idx1:idx2]
		individual[idx1:idx2] = [] #remove part
		
		idx3 = random.randint(0, len(individual))
		individual[idx3:idx3] = col
		
		comp(individual, basis,"eject-insert part with len<15")
		
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
		
		comp(individual, basis,"double swap")
		
	elif seed==6:
		#~ 
		#select random two, put them at selected place
		elts=[]
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
		
		comp(individual, basis,"eject two-insert seq")
		
	elif seed==14:
		#~ 
		#select random two, put them at selected place
		elts=[]
		for i in range(1,random.randint(2,6)):
			elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
		
		comp(individual, basis,"eject random-insert seq")
		#~ 
	elif seed==15:
		#no mutation
		pass
	elif seed==11:
		#~ 
		#select random three, put them at selected place
		elts=[]
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
		
		comp(individual, basis,"eject three-insert seq")
		
	elif seed==12:
		#~ 
		#select random four, put them at selected place
		elts=[]
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
		
		comp(individual, basis,"eject four-insert seq")
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
		comp(individual, basis,"step ahead swap")
	
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

#~ bestfit = genetic_algorithm(individual, fitness, mutate, crossover, 120, 40, 5000, 0.5)


# 3-fold cross-validation :))
bestfit1 = genetic_algorithm(individual, fitness, mutate, crossover, 125, 100, 3500, 0.5)
bestfit2 = genetic_algorithm(individual, fitness, mutate, crossover, 125, 100, 3500, 0.5)
bestfit3 = genetic_algorithm(individual, fitness, mutate, crossover, 125, 100, 3500, 0.5)

avg = str((bestfit1+bestfit2+bestfit3)/3.0)

print(SEED1, SEED2, bestfit1,bestfit2," avg=", avg)



with open("scores_SEED1_SEED2.txt","w") as f:
	f.write(str(SEED1)+","+str(SEED2)+","+str(bestfit1)+","+str(bestfit2)+","+str(bestfit3)+","+avg+"\n")
