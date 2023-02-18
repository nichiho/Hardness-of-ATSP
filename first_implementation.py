import numpy as np
import numpy.ma as ma

from LittlesAlgorithm.algorithm import get_minimal_route
from generate_matrices import generate_matrix_log_norm, save_matrix

matrix1 = generate_matrix_log_norm(4, 10, 2)
save_matrix(matrix1, 4, 10, 2, 1)

print(matrix1)

iterations, optimal_route, optimal_cost = get_minimal_route(matrix1)

print(iterations)
print(optimal_route)
print(optimal_cost)