# Import packages
import numpy as np
import random
import time

# Import files
import sys
sys.path.insert(1, "..")
from littles_algorithm.algorithm import get_minimal_route

# Hill-climbing method: 

# 1. Make a random matrix
# 2. Calculate the shortest tour & measure and save the run-tume of Little's algorithm
# 3. Mutate the matrix (change a single number)
# 4. Calculate the shortest tour & measure the run-time of Little's algorithm
# 5. 
# (a) If the new run time > old run time, go to #3
# (b) If the new run time <= old run time, revert to the older matrix, then go to #3

def mutate_matrix(matrix, n_cities, max_value):
    
    matrix_new = matrix.copy()
    # For the future: mutation can be done by modifying: adding by a value, by a certain percentage, etc.
        # Disadvantage: If we start with small numbers, the values will stay small for a long time
        # Replacing by a random value: no bias
    # Not doing that for now because replacing by a random value shouldn't change the output by much at the moment

    # Draw a sample of two numbers, random.sample makes sure the two numbers are not equal
    [x, y] = random.sample(range(1, n_cities), 2)
    old_value = matrix[x][y]
    
    # Matrice elements are random number between 0 and max_value
    new_value = random.randint(0, max_value)
    matrix_new[x][y] = new_value
    
    return x, y, matrix_new

def hill_climbing(n_cities, max_value, n_iterations):
    
    # A list of all the matrices
    mtx_list = []
    
    # A list of the run-time for each matrix
    run_time_list = []
    
    # A list of the performance (number of recursions) for each matrix
    performance_list = []
    
    # A list of whether each matrix in mtx_list is used or not
    used_or_not = []
    
    # A list of tuples of the index of the matrix mutated ((0, 0) if not mutated)
    indices = []
    
    # 1. Make a random matrix
    
    # Matrice elements to be a random number between 0 and max_value
    # (Same as Zhang & Khorfs a study of the complexity transitions on the ATSP)
    mtx_1 = np.random.randint(0, max_value, size = (n_cities, n_cities)).astype(float)
    np.fill_diagonal(mtx_1, np.inf)
    mtx_list.append(mtx_1)
    used_or_not.append(True)
    indices.append((0, 0))
    
    #2. Calculate the shortest tour & measure and save the performance of Little's algorithm
    run_time_list_1 = get_minimal_route(mtx_1)[0]
    run_time_list.append(run_time_list_1)
    
    performance_1 = get_minimal_route(mtx_1)[2]
    performance_list.append(performance_1)
    
    try:
        for i in range(0, n_iterations):
            # print(i)

            # 3. Mutate the matrix (change a single number)
            x, y, mtx_2 = mutate_matrix(mtx_1, n_cities, max_value)
            indices.append((x, y))
            mtx_list.append(mtx_2)
            
            # 4. Calculate the shortest tour & measure the performance (time) of Little's algorithm
            run_time_list_2 = get_minimal_route(mtx_2)[0]
            run_time_list.append(run_time_list_2)
            
            performance_2 = get_minimal_route(mtx_2)[2]
            performance_list.append(performance_2)
            
            # 5. 
            # (a) If the new performance >= old performance
            if performance_2  >= performance_1:
                # new matrix becomes mtx_1, mutate from that
                mtx_1 = mtx_2.copy()
                performance_1 = performance_2
                run_time_list_1 = run_time_list_2
                used_or_not.append(True)
            
            # (b) If the new performance < old performance, revert to the older matrix
            else:
                # Don't need to do anything, just repeat with mtx_1
                used_or_not.append(False)
        
    except KeyboardInterrupt:
        pass
    
    return mtx_list, run_time_list, performance_list, used_or_not, indices

# Function to automatically run n_iterations of hill_climbing
def hill_climbing_many_iterations(n_hill_climbing_iterations, n_cities, max_value, n_iterations):
    
    list_mtx_list = []
    list_run_time_list = []
    list_performance_list = []
    list_used_or_not = []
    list_indices = []

    try:
        for i in range(0, n_hill_climbing_iterations):
            start_time = time.time()
            
            mtx_list, run_time_list, performance_list, used_or_not, indices = hill_climbing(n_cities, max_value, n_iterations)
            
            list_mtx_list.append(mtx_list)
            list_run_time_list.append(run_time_list)
            list_performance_list.append(performance_list)
            list_used_or_not.append(used_or_not)
            list_indices.append(indices)
            
            end_time = time.time()
            
            print("Finished ", i + 1, " iterations in ", end_time - start_time, "seconds!")
        
    except KeyboardInterrupt:
        pass

    return list_mtx_list, list_run_time_list, list_performance_list, list_used_or_not, list_indices