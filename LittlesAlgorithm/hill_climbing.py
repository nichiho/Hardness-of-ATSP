# Import packages
import numpy as np
import random

# Import files
from LittlesAlgorithm.algorithm import get_minimal_route
from generate_matrices import generate_matrix_log_norm

# Hill-climbing method: 

# 1. Make a random matrix
# 2. Calculate the shortest tour & measure and save the run-tume of Little's algorithm
# 3. Mutate the matrix (change a single number)
# 4. Calculate the shortest tour & measure the run-time of Little's algorithm
# 5. 
# (a) If the new run time > old run time, go to #3
# (b) If the new run time <= old run time, revert to the older matrix, then go to #3

def mutate_matrix(matrix):
    [x, y] = random.sample(range(0, 3), 2)
    matrix[x][y] = np.random.lognormal(np.log(mean) - 1/2 * sd**2, sd)
    return matrix

def hill_climbing(n_cities, mean, sd, n_iterations):
    mtx_list = []
    run_time_list = []
    used_or_not = []
    
    # 1. Make a random matrix
    mtx_1 = generate_matrix_log_norm(n_cities, mean, sd)
    mtx_list.append(mtx_1)
    used_or_not.append(True)
    
    #2. Calculate the shortest tour & measure and save the run-tume of Little's algorithm
    run_time_1 = get_minimal_route(mtx_1)[2]
    run_time_list.append(run_time_1)
    
    for i in range(0, n_iterations):
    
        # 3. Mutate the matrix (change a single number)
        mtx_2 = mutate_matrix(mtx_1)
        print(mtx_2)
        mtx_list.append(mtx_2)
        
        # 4. Calculate the shortest tour & measure the run-time of Little's algorithm
        run_time_2 = get_minimal_route(mtx_2)[2]
        
        # 5. 
        # (a) If the new run time > old run time, go to #3
        # (b) If the new run time <= old run time, revert to the older matrix, then go to #3
        if run_time_2  > run_time_1:
            # new matrix becomes mtx_1, mutate from that
            mtx_1 = mtx_2.copy()
            run_time_1 = run_time_2
            used_or_not.append(True)
        
        if run_time_2 <= run_time_1:
            # Don't need to do anything, just repeat with mtx_1
            used_or_not.append(False)
    
    return mtx_list, run_time_list, used_or_not
        
        
mtx_list, run_time_list, used_or_not = hill_climbing(4, 10, 2, 10)

import matplotlib.pyplot as plt
plt.plot(run_time_list)
plt.show()