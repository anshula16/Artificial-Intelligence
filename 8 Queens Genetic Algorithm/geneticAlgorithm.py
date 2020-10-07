import numpy as np
import sys
import BoardPosition as bp

nQueens = 8
POPULATION = None
MUTATE = np.random.random()
MUTATE_FLAG = True
STOP_CTR = 28
MAX_ITER = 100000

def calculateFitness(sequence_of_queens):
    '''
    Returns: 28 - number of conflicts
    To test for conflicts, we check:
    --> Row conflicts
    --> Column conflicts
    --> Diagonal conflicts

    The ideal case can yeild upto 28 arrangements of non-attacking pairs.
    There are 28 pairs of different queens, smaller column first, all together, so solutions have fitness 28.
    7 + 6 + 5 + 4 + 3 + 2 + 1 = 28
    '''

    row_clashes = 0 # each queen is in different rows.
    col_clashes = len(sequence_of_queens) - len(np.unique(sequence_of_queens))  # if sequence has repeated values, it means that these different queens are in the same column. 

    diagonal_clashes = 0

    for i in range(len(sequence_of_queens)):
        for j in range(i, len(sequence_of_queens)):
            if i != j:
                row_diff = abs(i - j)
                col_diff = abs(sequence_of_queens[i] - sequence_of_queens[j])

                if row_diff == col_diff:
                    diagonal_clashes += 1

    total_clashes = row_clashes + col_clashes + diagonal_clashes
    return 28 - total_clashes

def generateChromosome():
    '''
    Randomly generate chromosomes
    '''

    global nQueens

    initial_distribution = np.arange(nQueens) # Return evenly spaced values within a given interval.
    np.random.shuffle(initial_distribution)
    return initial_distribution

def generatePopulation(population_size = 100):
    '''
    Create population_size number of board positions.
    Set sequence and fitness value of each board position.
    '''
    global POPULATION

    POPULATION = population_size

    population = [bp.BoardPosition() for _ in range(POPULATION)]

    for i in range(POPULATION):
        population[i].setSequenceOfQueens(generateChromosome())
        population[i].setFitness(calculateFitness(population[i].sequence_of_queens))

    return population

def setSurvival(population):
    '''
    Chances of survival is calculated for each member of the population.
    '''
    summation_of_fitness = np.sum(p.fitness for p in population)

    for each in population:
        each.setSurvival(each.fitness / (summation_of_fitness * 1.0))

def getParents(population):
    '''
    Parent is decided by random probability of survival.
    '''
    setSurvival(population)
    parent1, parent2 = None, None

    # 1st parent
    while True:
        parent1_random_survival = np.random.rand()
        parent1_random = [p for p in population if p.survival <= parent1_random_survival]
        
        try:
            index = np.random.randint(len(parent1_random))
            parent1 = parent1_random[index]
            break
        
        except:
            pass
        
    # 2nd parent
    while True:
        parent2_random_survival = np.random.rand()
        parent2_random = [p for p in population if p.survival <= parent2_random_survival]
        
        try:
            index = np.random.randint(len(parent2_random))
            parent2 = parent2_random[index]

            if parent1 != parent2:
                break
            continue
            
        except:
            pass
    
    if parent1 is not None and parent2 is not None:
        return parent1, parent2
    
    sys.exit(-1)

def reproduceCrossover(parent1, parent2):
    '''
    2 parents reproduce to form a child.
    Once parents having high fitness are selected, crossover essentially marks the recombining of genetic materials / chromosomes to produce a healthy offspring.
    '''
    n = len(parent1.sequence_of_queens)
    index = np.random.randint(n)

    child = bp.BoardPosition()
    
    child.sequence_of_queens = []
    child.sequence_of_queens.extend(parent1.sequence_of_queens[0 : index])
    child.sequence_of_queens.extend(parent2.sequence_of_queens[index : ])

    return child

def mutate(child):
    '''
    Mutation may or maynot occur. In case mutation occurs, it forces a random value of child to change, thereby shifting the algorithm in either a positive or negative route.

    --> According to genetic theory, a mutation will take place when there is an anomaly during cross over state.
    --> Since a computer cannot determine such anomaly, we can define the probability of developing such a mutation.
    '''
    prob = np.random.random()
    
    if prob < MUTATE:
        index = np.random.randint(nQueens)
        child.sequence_of_queens[index] = np.random.randint(nQueens)

    return child

def geneticAlgorithm(population):

    new_population = []

    for i in range(len(population)):
        parent1, parent2 = getParents(population)

        child = reproduceCrossover(parent1, parent2)

        if MUTATE_FLAG:
            child = mutate(child)
        
        child.setFitness(calculateFitness(child.sequence_of_queens))
    
        new_population.append(child)
    
    return new_population

def stop(population, iteration):
    '''
    Checks for stopping condition:
    - if solution is found
    - if maximum iterations are done
    '''
    fitness_vals = [p.fitness for p in population]

    if STOP_CTR in fitness_vals:
        return True
    
    if MAX_ITER == iteration:
        return True
    
    return False
