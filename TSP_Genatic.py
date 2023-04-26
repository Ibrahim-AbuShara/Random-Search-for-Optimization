import numpy as np
import pandas as pd
import math
import random
from copy import deepcopy
import matplotlib.pyplot as plt
import os
class Chromosome:
    def __init__(self, lst):
        self.road = lst
        self.cost = np.inf
        self.fitness = 1/self.cost
        
    
    def set_fitness(self, cost):
        self.cost = cost
        self.fitness = 1/cost

    def __repr__(self):
        return (f"list of cities:\n{str(self.road)}\nTotal Destance: {str(self.cost)} ")  
    
class City:
    def __init__(self, number, x, y):
        self.number = number
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"City:  {str(self.number)}  {str(self.x)}   {str(self.y)} \n"
    
    
    
def cost_function(chromosome, mat):
    total_cost = 0
    lst = chromosome.road
    for i, gene in enumerate(lst):
        if i == 0:
            continue
        total_cost += mat[gene.number][lst[i-1].number]
        
    total_cost += mat[lst[0].number][lst[-1].number]
    return total_cost

def initial_pob(lst_cities, n, dist_mat):  
    generation = []
    for i in range(n):
        chromosome = lst_cities.copy()
        chromosome=np.random.permutation(chromosome).tolist()
        chromosome = Chromosome(chromosome)
        cost = cost_function(chromosome, dist_mat)
        chromosome.set_fitness(cost)
        generation.append(chromosome)
    return generation


def calc_dist_matrix(data):
    n = len(data)
    mat = {} 
    for i,point in enumerate(data): 
        key = point.number
        mat[key] = {}
        for j in range(n):
            p2 = data[j]
            c = p2.number
            mat[key][c] = math.dist([point.x , point.y], [p2.x, p2.y])     
    return mat


def elite_selection(percent, pob):
    n = int(percent*len(pob))
    # choose most n fittest chromosomes
    sort = sorted(pob, key = lambda x: x.fitness, reverse=True)
    return sort[:n+1], sort[n+1:]

def random_selection(pob):
    return np.random.choice(pob)

def tournment_selection(pob, candidates_num):
    candidates = random.choices(pob, k=candidates_num)
    return max(candidates, key = lambda x: x.fitness)

def roulette_wheel_selection(pob):
    pob_fitness = sum([chromosome.fitness for chromosome in pob])
    chromosome_prob = [chromosome.fitness/pob_fitness for chromosome in pob]
    return np.random.choice(pob, p=chromosome_prob)


def swap_pc(c,p,range1,range2):
    for gene in range(range1, range2+1):
        # find the duplicated city
        dup = p.road[gene] 
        dup_i = [d.number for d in c.road].index(dup.number)
        c.road[gene], c.road[dup_i] = c.road[dup_i], c.road[gene]
        c.road[gene] = p.road[gene]
    return c

def singlePoint_crossover(p1, p2, dist_mat):
    ln = len(p1.road)
    # random split range
    range1 = random.randint(0,ln-1)
    range2 = random.randint(0,ln-1)
    if range1 > range2:
        range1, range2 = range2, range1
        
    # children
    c1 = deepcopy(p1)
    c2 = deepcopy(p2)
      
    c1=swap_pc(c1, p2, range1, range2)
    c2=swap_pc(c2, p1, range1, range2)
    
    c1.set_fitness(cost_function(c1, dist_mat)) 
    c2.set_fitness(cost_function(c2, dist_mat)) 
    return c1, c2

def seletion_and_crossover(prob, pob, n):
    candidates_num = 10
    new_pob = []
    while len(new_pob) < n:
        # random  selection
        parent1 = random_selection(pob)
        parent2 = random_selection(pob)
        
        # # tournment selection
        # parent1 = tournment_selection(pob, candidates_num)
        # parent2 = tournment_selection(pob, candidates_num)
        
        # # roulette wheel selection
        # parent1 = roulette_wheel_selection(pob)
        # parent2 = roulette_wheel_selection(pob)
        
        
        # singlePoint crossover
        rand= random.random()
        if rand< prob: 
            child1, child2 = singlePoint_crossover(parent1, parent2, dist_mat)
            new_pob.append(child1)
            new_pob.append(child2)
    return new_pob


def mutation(prob, pob, dist_mat):
    new_pob = []
    for i,chrom in enumerate(pob):
        c = deepcopy(chrom)
        rand= random.random()
        if rand< prob: 
            ln = len(chrom.road)
            gene1 = random.randint(0,ln-1)
            gene2 = random.randint(0,ln-1)
            c.road[gene1], c.road[gene2] = c.road[gene2], c.road[gene1]
#         
        c.set_fitness(cost_function(c, dist_mat)) 
        new_pob.append(c)
    return new_pob


def plot_map(data, chromosome):
    lst = []
    for city in chromosome.road:
        lst.append(city.number-1)
        
    lst.append(chromosome.road[0].number-1)
    for i in range(len(lst)):
        plt.plot(data.values[lst][:,0],data.values[lst][:,1],'*',color='green')
        df=np.array(data.values[lst[:i+1]])
        ax=plt.plot(df[:,0],df[:,1],lw=5,color="blue")
        plt.plot(data.values[lst[i]][0],data.values[lst[i]][1],'o',lw=10,color="red")
        plt.xlim(-90,30)
        plt.ylim(-50,30)
        plt.title(f"Traveling Salesman Problem Genatic Algo\nCity: {int(data.values[lst[i]][-1])}")
        plt.savefig(f"/home/ibrahim/projects/Random-Search-for-Optimization/gen_imgs/{i:003}",dpi=100,facecolor="white")
        plt.close()
    os.system("convert -delay 50 /home/ibrahim/projects/Random-Search-for-Optimization/gen_imgs/*.png tsp_gen.gif")
    os.system("gifview -a tsp_gen.gif ")
        
    
# ____Main______
df = pd.read_excel("15-Points.xlsx")
city_obj = [City(num,x,y) for num,x,y in zip(df['City'], df['x'], df['y'])]
n = len(city_obj)
pob_size = 100
itr_num=100
elite_ratio =0.05
crossover_ratio =.8
mutation_ratio =.5
dist_mat = calc_dist_matrix(city_obj)
gen = initial_pob(city_obj, pob_size, dist_mat)
 
for i in range(itr_num):
    new_pob = []
    elite, rest = elite_selection(elite_ratio, gen) 
    crossover_count = len(rest)
    crossed_over = seletion_and_crossover(crossover_ratio, gen, crossover_count) 
    mutated = mutation(mutation_ratio, crossed_over, dist_mat) 
    new_pob.extend(elite)
    new_pob.extend(mutated)
    gen = new_pob.copy()
    elite_ratio=elite_ratio+.01
      
best = max(gen, key = lambda x: x.fitness)
print(best)
print("Wait for GIF to finish...")
plot_map(df, best)