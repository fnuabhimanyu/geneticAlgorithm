import random
import numpy as np
import operator

def create_population(sizePopulation):
	pop = []
	for _ in range(sizePopulation):
		pop.append(np.random.rand(2) * 2 - 1)
	return (pop)

def fitness_function(l):
	for _ in range(2):
		sum = -l[0]**2+1
		fitness_value = sum
	return(fitness_value)



def pop_performance(pop):
	f = []
	pop_new = []
	count = 0
	for i in pop:
		f.append([fitness_function(i),count])
		count = count+1
	#print(f)
	f.sort(key = operator.itemgetter(0),reverse = True)
	best_fitness = f[0][0]
	best_set = pop[f[0][1]]
	
	for j in range(len(pop)):
		pop_new.append(pop[f[j][1]])
	return pop_new,best_fitness,best_set

def select_pop(pop_new,sizePopulation,retain):
	pop = []
	for i in range(retain):
		pop.append(pop_new[i])
	for i in range(sizePopulation-retain):
		pop.append(np.random.rand(2) * 2 - 1)
	np.random.shuffle(pop)
	return pop
	
def create_children(individual1,individual2):
	child1 = []; child2 = [];
	if (np.random.rand()<0.5):
		for i in range(int(len(individual1)/2)):
			child1.append(individual1[i])
			child1.append(individual2[len(individual1)-i-1])
			child2.append(individual1[len(individual1)-i-1])
			child2.append(individual2[i])
	else:
		for j in range(int(len(individual1)/2)):
			child1.append(individual2[j])
			child1.append(individual1[j])
			child2.append(individual2[len(individual1)-j-1])
			child2.append(individual1[len(individual1)-j-1])
			
	return (child1,child2)

def new_pop(pop):
	#print(len(pop)/2)
	pop_new = []
	for i in range(int(len(pop)/2)):
		child1,child2 = create_children(pop[i],pop[len(pop)-i-1]) 
		#print(child1,child2)
		pop_new.append(child1)
		pop_new.append(child2)
	return pop_new	
	
def mutate_child(individual):
	if (np.random.rand() < 0.5):
		individual[0] = individual[0] + 10*0.01
		#print(individual[0])
	else:
		individual[len(individual)-1] = individual[len(individual)-1] + 10*0.01
		#print(np.random.rand())
		#print(individual[len(individual)-1])
		#print(individual)
	return individual

def mutate_pop(pop):
	pop_new = []
	for i in range(int(len(pop))):
		child1 = mutate_child(pop[i]) 
		#print(child1)
		pop_new.append(child1)
	return pop_new	

'''a = create_population(8)
print(a)
print("\n")
print(pop_performance(a))
print("\n")
b = (select_pop(pop_performance(a),8,4))
print (b)
print("\n")
c= new_pop(b)
print(mutate_pop(c))'''



