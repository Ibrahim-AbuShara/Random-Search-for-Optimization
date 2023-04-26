import numpy as np
import matplotlib.pyplot as plt

import numpy as np

class Particle:
    def __init__(self, minimum_position, maximum_position,cost_function):

        self.position = np.random.uniform(minimum_position, maximum_position).reshape(-1, 1)
        self.velocity = np.zeros(self.position.shape)
        self.cost = cost_function(self.position)
        self.best_cost = self.cost
        self.best_position = self.position.copy()

class GlopalParticle:

    def __init__(self) -> None:

        self.best_position = []
        self.cost = np.inf

def linear_cost(position):
    global target_label
    global features
    predicted_label = position[0] * features + position[1]
    error_vector = predicted_label - target_label
    cost = (np.linalg.norm(error_vector) ** 2) / (len(target_label)*2)
    return cost
#problem Defineiton 
features = np.linspace(-5,5,1000).reshape(-1,1)
target_label = -2 * features + 3 + np.random.rand(*features.shape)
#y_pred = particle.pos[0] + x * particle.pos[1]
cost = lambda x : (x[0] - 2) ** 2 + (x[1] - 4)**2

nVar = 2
var_minimum = [-5, -10]
var_maximum = [5, 10]
# PS Parameters
w = 1
c1, c2 = 2, 2
damp = 0.9
iterations = 200
pop_size = 50 
# intialization

global_best = GlopalParticle()
particles = [None] * pop_size

for i in range(pop_size):
    particles[i] = (Particle(var_minimum, var_maximum, linear_cost))
    if particles[i].cost < global_best.cost:
        global_best.best_position = particles[i].position.copy()
        global_best.cost = particles[i].cost

for iteration in range(iterations):

    for i in range(pop_size):
        particles[i].velocity = w * particles[i].velocity + c1 * np.random.rand() * (particles[i].best_position - particles[i].position) + c2 * np.random.rand() * (global_best.best_position - particles[i].position)

        particles[i].position = particles[i].position + particles[i].velocity
        particles[i].cost = linear_cost(particles[i].position)
        if particles[i].cost < particles[i].best_cost:
            particles[i].best_position = particles[i].position.copy()
            particles[i].best_cost = particles[i].cost
            if particles[i].cost < global_best.cost:
                global_best.best_position = particles[i].position.copy()
                global_best.cost = particles[i].cost
    
    w = w * damp
    print(f"iter {iteration} : {global_best.cost}")

print(f"best answer = {global_best.best_position}")


# Plotting the data and the best fit line
plt.figure()
plt.scatter(features, target_label, label='Data')
plt.plot(features, global_best.best_position[0] * features + global_best.best_position[1], color='red', label='Best Fit Line')
plt.legend()
plt.xlabel('Features')
plt.ylabel('Target Label')
plt.title('Particle Swarm Optimization for Linear Regression')
plt.show()
