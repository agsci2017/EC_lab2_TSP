# EC_lab2_TSP

1. Утилита 1_TSP_gen.py преобразует *.tsp файл(немного измененный - удален префикс, добавлен заголовок) в матрицу расстояний(Matrix.p).
2. 2_TSP.py(использует модуль genetic_algorithm.py) считывает Matrix.p и ищет кратчайший тур. Лучший из туров можно скопировать из окна консоли.
3. 3_TSP_viz.py визуализирует тур. Тур задается в переменной way, в коде.

4. FMS_one_mutation.py используя TSP_template.py, генерирует множество файлов TSP_seed_*.py, содержащих использование одной определенной мутации. Также, генерирует файл best.sh - скрипт запуска и распараллеливания поиска наилучшей мутации. Усредненный результат трех симмуляций выводится в файлы вида scores_1_1.txt.

Первая строка в функции mutate должна иметь вид:
```
seed=random.choice([SEED1])
или
seed=random.choice([17,SEED1]) #для поиска второй, после нахождения наулучшей первой
```

5. FMS_two_mutations.py используя TSP_template.py, генерирует множество файлов TSP_seed_*.py, содержащих использование двух определенных мутаций. Также, генерирует файл best.sh - скрипт запуска и распараллеливания поиска наилучших мутаций. Усредненный результат трех симмуляций выводится в файлы вида scores_1_3.txt.

Первая строка в функции mutate должна иметь вид:
```
seed=random.choice([SEED1,SEED2])
```

Пример отчета для двух мутаций (по параметрам TSP_template.py) находится в **0_SCORES.csv**.

# Кратчайший тур

![alt](Tour.png)

Полученный результат = 582.

Лучший результат на сайте = 564.

http://www.math.uwaterloo.ca/tsp/vlsi/xqf131.tour.html

```python
way = [8, 2, 3, 9, 10, 4, 11, 23, 38, 39, 40, 41, 42, 24, 43, 44, 61, 60, 59, 73, 72, 80, 86, 85, 84, 83, 79, 76, 71, 70, 66, 67, 63, 58, 57, 56, 62, 65, 69, 75, 64, 68, 77, 78, 81, 82, 87, 88, 92, 94, 90, 91, 95, 96, 97, 104, 103, 111, 110, 109, 115, 119, 116, 120, 117, 122, 129, 128, 127, 131, 126, 125, 124, 106, 107, 113, 108, 99, 102, 101, 100, 105, 114, 118, 121, 130, 123, 112, 98, 93, 89, 74, 53, 45, 46, 54, 55, 47, 48, 49, 50, 51, 52, 36, 37, 22, 35, 34, 21, 33, 32, 31, 30, 20, 29, 28, 27, 26, 19, 25, 17, 16, 15, 14, 18, 13, 5, 12, 6, 1, 7] #582. (best=564)
```

# Эволюция

Особенности:
0. Лучшие родители оставляют больше потомков.
```
		for osob in range(1,10):
			offspring.append(crossover(parents[0], parents[osob]))
		for osob in range(2,10):
			offspring.append(crossover(parents[1], parents[osob]))
		for osob in range(3,10):
			offspring.append(crossover(parents[2], parents[osob]))
		for osob in range(5,10):
			offspring.append(crossover(parents[4], parents[osob]))
```
1. Одна мутация и вторая с 50% вероятностью.
```
        for i in range(len(parents)):
			if mutation_rate > random.random():
				parents[i] = mutate(parents[i])
		if random.randint(0,1)==0:
			for i in range(len(parents)):
				if mutation_rate > random.random():
					parents[i] = mutate(parents[i])
```
2. Сохраняем одного лучшего родителя перед мутацией
```
saving1 = parents[:1]
```
3. Родители мутируют после кросс-овера, вместе с потомками. 1 родитель не мутирует.

# Мутации

```
  #Перемещивание произвольно выбранной части
	if seed==0:
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, min(idx1+55, len(individual)-1))
		
		col = individual[idx1:idx2]
		random.shuffle(col)
		individual[idx1:idx2]=col
	
  #Обмен двух случайных элементов
	elif seed==1:
		#swap
		idx1 = random.randint(0, len(individual)-1)
		idx2 = random.randint(0, len(individual)-1)
		
		tmp = individual[idx1]
		
		individual[idx1] = individual[idx2]
		individual[idx2] = tmp
	
  #Обмен двух случайных пар
	elif seed==2:
		#swap 2
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(0, len(individual)-2)
		if abs(idx2-idx1)>5:
			col1 = individual[idx1:idx1+1]
			col2 = individual[idx2:idx2+1]
			individual[idx2:idx2+1] = col1
			individual[idx1:idx1+1] = col2
  #Оборачивание участка
	elif seed==3:
		#reverse part
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)

		col = individual[idx1:idx2]
		
		individual[idx1:idx2]=reversed(col)
	
  #Сортировка участка
	elif seed==4:
		#sort part
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)

		col = individual[idx1:idx2]
		
		individual[idx1:idx2]=sorted(col)
	
  #Извлечение участка и вставка его в произвольном месте
	elif seed==5:
		
		par = copy.deepcopy(individual)
		
		#big swap
		idx1 = random.randint(0, len(individual)-2)
		idx2 = random.randint(idx1+1, len(individual)-1)
		
		col = individual[idx1:idx2]
		individual[idx1:idx2] = [] #remove part
		
		idx3 = random.randint(0, len(individual))
		individual[idx3:idx3] = col
  
  #два последовательных случайных обмена
	elif seed==6:
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
  
  #выбор двух случайных элементов и размещение их подряд в случайном месте
	elif seed==7:
		#select random two, put them at selected place
		elts=[]
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		elts.append(individual.pop(random.randint(0,len(individual)-1)))
		
		idx1 = random.randint(0, len(individual)-1)
		
		individual[idx1:idx1] = elts
```

# Кроссовер

```
def crossover(parent1, parent2):

	#Инициализация массива
	child = [0]*len(parent1)
	
	#Пустой массив, заполненный None
	for x in range(0,len(child)):
		child[x] = None

	start_pos = random.randint(0,len(parent1))
	end_pos = random.randint(0,len(parent1))
  
  #наследование части элементов первого родителя
	if start_pos < end_pos:
		# start->end
		for x in range(start_pos,end_pos):
			child[x] = parent1[x]
	elif start_pos > end_pos:
		#end->start
		for i in range(end_pos,start_pos):
			child[i] = parent1[i]

	#замена оставшихся None элементами второго родителя
	for i in range(len(parent2)):
		if not parent2[i] in child:
			for x in range(len(child)):
				if child[x] == None:
					child[x] = parent2[i]
					break

	return child
```

# Fitness-функция

Оценка тура имеет вид: 913.82

```
def fitness(individual):
	
	#sum
	cost = 0
	
	for i in range(0, len(individual)-1):
		cost += distMatrix[individual[i]][individual[i+1]]
	cost += distMatrix[len(individual)-1][0]
	
	return cost
```

# Генерация особи

```
def individual():
	lst = list(range(1,len(distMatrix)))
  #случайное перемешивание
	random.shuffle(lst)
	
	return lst
```
