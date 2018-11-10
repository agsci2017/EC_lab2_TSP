import random
import pickle



def sort_by_fitness(func,pop):
	lst = sorted(zip(map(func, pop), pop), key=lambda t: t[0])
	lst = list(map(lambda v: v[1], lst))
	#~ print(fit(lst[0]))
	#~ print(func(lst[-1]))
	return lst

def generate_individuals(func, n):
	return list(map(lambda v: func(), range(n)))

import copy

def genetic_algorithm(individual, fitness, mutate, crossover, n_individuals=10, retain=6, epochs=10, mutation_rate=0.2):
	
	population = generate_individuals(individual, n_individuals)
	
	print(len(list(population)))
	import pickle
	#~ population = pickle.load( open( "population.p", "rb" ) )
	
	#~ population.append([11, 4, 10, 9, 3, 2, 8, 7, 1, 6, 12, 5, 13, 18, 14, 15, 16, 17, 25, 26, 27, 19, 20, 21, 22, 23, 24, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 46, 45, 53, 74, 68, 64, 54, 55, 47, 48, 49, 50, 51, 52, 57, 56, 62, 65, 69, 66, 70, 76, 71, 67, 63, 58, 59, 60, 61, 73, 72, 80, 79, 83, 84, 85, 86, 90, 91, 95, 96, 97, 104, 103, 111, 110, 99, 94, 92, 88, 87, 82, 81, 78, 75, 77, 89, 93, 98, 100, 105, 101, 102, 106, 107, 113, 108, 109, 115, 119, 116, 120, 117, 122, 129, 128, 127, 126, 125, 124, 121, 118, 114, 112, 123, 130, 131])
	
	#GENERATION FINISHED
	for e in range(epochs):
		#mutation_rate-=0.001
		#print(mutation_rate)
		#~ print(len(population))
		
		population = sort_by_fitness(fitness, population)
		
		#~ print(len(population))
		
		print('Gen #{} Best: fitness ({}) individual ({})'.format(e, fitness(population[0]), population[0]))

		parents = population[:retain]
		
		#новые случайные особи могут иметь последовательность, которая может улучшить score
		#поэтому, позволяем им участвовать в кросс-овере
		for kk in range(0,30):
			parents.append(individual())

		n_offspring = n_individuals - retain

		offspring = []
		while len(offspring) < n_offspring:
			male, female = random.randint(0, len(parents)-1), random.randint(0, len(parents)-1)
			if male != female:
				offspring.append(crossover(parents[male], parents[female]))
		
		#можно сделать чтобы мутировали родители(parents), которые оставили потомство
		#score будет меняться скачкообразно
		saving = parents[:3]
		
		for i in range(len(parents)):
			if mutation_rate > random.random():
				parents[i] = mutate(parents[i])

		population = parents + offspring + saving


	population = sort_by_fitness(fitness, population)
	
	pickle.dump( population, open( "population.p", "wb" ) )

	return population[0] 
	
