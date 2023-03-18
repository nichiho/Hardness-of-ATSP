# Import packages
import numpy as np
import random

# Import files
from LittlesAlgorithm.algorithm import get_minimal_route

# Hill-climbing method: 

# 1. Make a random matrix
# 2. Calculate the shortest tour & measure and save the run-tume of Little's algorithm
# 3. Mutate the matrix (change a single number)
# 4. Calculate the shortest tour & measure the run-time of Little's algorithm
# 5. 
# (a) If the new run time > old run time, go to #3
# (b) If the new run time <= old run time, revert to the older matrix, then go to #3

def mutate_matrix(matrix, max_value):
    
    # For the future: mutation can be done by modifying: adding by a value, by a certain percentage, etc.
        # Disadvantage: If we start with small numbers, the values will stay small for a long time
        # Replacing by a random value: no bias
    # Not doing that for now because replacing by a random value shouldn't change the output by much at the moment
    
    # Matrice elements are random number between 1 and max_value
    [x, y] = random.sample(range(0, 3), 2)
    matrix[x][y] = random.randint(1, max_value)
    return matrix

def hill_climbing(n_cities, max_value, n_iterations):
    mtx_list = []
    run_time_list = []
    used_or_not = []
    
    # 1. Make a random matrix
    
    # Matrice elements to be a random number between 1 and max_value
    # (Same as Zhang & Khorfs a study of the complexity transitions on the ATSP)
    mtx_1 = np.random.randint(1, max_value, size = (n_cities, n_cities))
    mtx_list.append(mtx_1)
    used_or_not.append(True)
    
    #2. Calculate the shortest tour & measure and save the run-tume of Little's algorithm
    run_time_1 = get_minimal_route(mtx_1)[2]
    run_time_list.append(run_time_1)
    
    for i in range(0, n_iterations):
    
        # 3. Mutate the matrix (change a single number)
        mtx_2 = mutate_matrix(mtx_1, max_value)
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