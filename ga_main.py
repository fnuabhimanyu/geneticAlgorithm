import random
import numpy as np
import operator
import ga

sizePopulation = 8;
sizeElement = 2;
sizeRetain = 4;
iterations = 10000;
bf = []
a = ga.create_population(sizePopulation)
#print(a)

for i in range(iterations):
	
	#print(a)
	#print("\n")
	#print(pop_performance(a))
	#print("\n")
	pop_new,best_fitness,best_set = ga.pop_performance(a)
	bf.append(best_fitness)
	b = (ga.select_pop(pop_new,sizePopulation,sizeRetain))
	#print (b)
	#print("\n")
	#c= ga.new_pop(b)
	#print(mutate_pop(c))
	a = ga.mutate_pop(ga.new_pop(b))

print(bf[len(bf)-1])
print("\n")
print(best_set)
