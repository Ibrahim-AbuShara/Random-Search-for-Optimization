import numpy as np
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(1)
X = np.random.rand(50, 1)
y = 2 + 3 * X + np.random.rand(50, 1)

# Define objective function for linear regression
def objective_function(X, y, theta):
    m = len(y)
    y_pred = np.dot(X, theta)
    error = y_pred - y
    mse = np.mean(error**2)
    return mse

# Simulated Annealing algorithm
def simulated_annealing(X, y, n_iterations, temp, alpha):
    # Initialize theta with random values
    theta = np.random.rand(2, 1)
    best_theta = theta
    best_cost = objective_function(X, y, theta)
    costs = []

    for i in range(n_iterations):
        # Generate new candidate solution
        candidate_theta = theta + np.random.randn(2, 1) * temp
        candidate_cost = objective_function(X, y, candidate_theta)

        # Calculate Metropolis acceptance criterion
        metropolis = np.exp((best_cost - candidate_cost) / temp)

        # Accept or reject the candidate solution
        if candidate_cost < best_cost or np.random.rand() < metropolis:
            theta = candidate_theta
            best_cost = candidate_cost

        # Update best solution
        if candidate_cost < objective_function(X, y, best_theta):
            best_theta = candidate_theta

        # Update temperature
        temp *= alpha

        # Store costs for plotting
        costs.append(best_cost)

    return best_theta, costs

# Define parameters for Simulated Annealing
n_iterations = 1000
temp = 1.0
alpha = 0.99

# Add bias term to feature matrix X
X_b = np.c_[np.ones((50, 1)), X]

# Perform Simulated Annealing for linear regression
best_theta, costs = simulated_annealing(X_b, y, n_iterations, temp, alpha)

# Print best theta
print("Best theta: ", best_theta)

# Plot input data points
plt.scatter(X, y, c='b', label='Input Data')

# Plot best-fit line
X_plot = np.linspace(0, 1, 100)
y_plot = best_theta[0] + best_theta[1] * X_plot
plt.plot(X_plot, y_plot, c='r', label='Best-fit Line')

plt.xlabel('X')
plt.ylabel('y')
plt.title('Linear Regression with Simulated Annealing')
plt.legend()
plt.show()
plt.plot(costs)
plt.xlabel('Iteration')
plt.ylabel('Objective Function Value')
plt.title('cost')
plt.show()