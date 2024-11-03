import argparse
import json
import random

def value_knapsack(knapsack, packing ):
    """Function calculating knapsack value"""
    value = 0
    weight = 0
    for i,item in enumerate(knapsack['items']):
        value += item['value'] if packing[i] == 1 else 0
        weight += item['weight'] if packing[i] == 1 else 0
        if weight > knapsack['capacity']:
            return 0
    return value

def hill_climbing(goal, random_solution, random_neighbour, iterations):
    current =  random_solution()
    print("    ", current)
    for i in range(iterations):
        neighbour = random_neighbour(current.copy())
        print(" ?? ", neighbour, goal(neighbour))
        if goal(neighbour) > goal(current):
            print(" ++ ", neighbour, goal(neighbour))
            current = neighbour
    print(" >> ", current, goal(current))
    return current

def select_roulette_rule(fitnesses):
    sum_fit = 0
    selected = []
    for f in fitnesses: sum_fit += f
    for i in range(len(fitnesses)):
        r = random.random()*sum_fit
        sf = 0
        for j in range(len(fitnesses)):
            f = fitnesses[j]
            sf+=f
            if sf>r:
                selected.append(j) # dopisujemy indeks osobnika
                break
    return selected

def crossover(a,b):
    # cross_point = random.randint(0,len(a)-1)
    # new_a = [ a[i] if i < cross_point else b[i] for i in range(len(a)) ]
    # new_b = [ b[i] if i < cross_point else a[i] for i in range(len(a)) ]
    # return new_a, new_b
    m = random.randint(0,len(a)-1)
    n = random.randint(m, len(a) - 1)

    new_a = a[:m] + b[m:n+1] + a[n+1:]
    new_b = b[:m] + a[m:n+1] + b[n+1:]

    return new_a,new_b

def mutate_probability(element,mutation_rate):
    for i in range(len(element)):
        if random.random() < mutation_rate:
            element[i] = 1 - element[1] #zmieniamy element na przeciwny 0->1, 1->0
    return element

def genetic_algorithm(fitness, random_solution, iterations, pop_size, p_mutation, p_crossover):
    # Punkt2 - p_mutation, potem p_crossover w 3
    population = [ random_solution() for _ in range(pop_size) ]

    for i in range(iterations): # warunek zakonczenia do poprawy
        fitnesses = [ fitness(population[i]) for i in range(len(population)) ]
        print("f:", fitnesses)
        selected = select_roulette_rule(fitnesses)
        print("  ", selected)
        new_population = []
        for i in range(int(len(population)/2)):
            a = population[selected[i*2]]
            b = population[selected[i*2+1]]

            if random.random() < p_crossover: #z jakąś szansą crosujemy
                a, b = crossover(a, b)

            new_population.append(mutate_probability(a,p_mutation))
            new_population.append(mutate_probability(b,p_mutation))
        # todo: mutation and probabilites of mutation and crossover
        population = new_population
    return population



def random_neighbour_packing(packing):
    for i in range(len(packing)):
        packing[i] = packing[i] if random.randint(0,1) == 1 else 1 - packing[i]
    return packing

def random_packing(n):
    return [ random.randint(0,1) for _ in range(n) ]


def main(): #argparse=https://docs.python.org/3/library/argparse.html
    parser = argparse.ArgumentParser(prog="Algorytm Generyczny", description="Generic Algorythm", epilog="Write name of file")
    parser.add_argument('filename') #should be main.json
    args = parser.parse_args()

    with open(args.filename, 'r') as knapsack_file:
        knapsack = json.load(knapsack_file)

    #packing = [1,0,1,1]
    result = hill_climbing(lambda x: value_knapsack(knapsack, x ),
                           lambda: random_packing(len(knapsack['items'])),
                           random_neighbour_packing,
                           50)
    print(result)

    genetic_algorithm(lambda x: value_knapsack(knapsack, x ),
                      lambda: random_packing(len(knapsack['items'])),
                      100,
                      50, 0.5, 0.5)
    #print(knapsack,packing)
    #print(value_knapsack(knapsack, packing))

if __name__ == "__main__":
    main()
