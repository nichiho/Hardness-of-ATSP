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

def mutate_matrix(matrix, n_cities, max_value):
    
    matrix_new = matrix.copy()
    # For the future: mutation can be done by modifying: adding by a value, by a certain percentage, etc.
        # Disadvantage: If we start with small numbers, the values will stay small for a long time
        # Replacing by a random value: no bias
    # Not doing that for now because replacing by a random value shouldn't change the output by much at the moment

    # Draw a sample of two numbers, random.sample makes sure the two numbers are not equal
    [x, y] = random.sample(range(0, n_cities), 2)
    
    # Matrice elements are random number between 1 and max_value
    matrix_new[x][y] = random.randint(1, max_value)
    
    return matrix_new

def hill_climbing(n_cities, max_value, n_iterations):
    
    # A list of all the matrices
    mtx_list = []
    
    # A list of the performance for each matrix
    performance_list = []
    
    # A list of whether each matrix in mtx_list is used or not
    used_or_not = []
    
    # 1. Make a random matrix
    
    # Matrice elements to be a random number between 1 and max_value
    # (Same as Zhang & Khorfs a study of the complexity transitions on the ATSP)
    mtx_1 = np.random.randint(1, max_value, size = (n_cities, n_cities)).astype(float)
    np.fill_diagonal(mtx_1, np.inf)
    mtx_list.append(mtx_1)
    used_or_not.append(True)
    
    #2. Calculate the shortest tour & measure and save the performance of Little's algorithm
    performance_1 = get_minimal_route(mtx_1)[0]
    performance_list.append(performance_1)
    
    try:
        for i in range(0, n_iterations):
            print(i)

            # 3. Mutate the matrix (change a single number)
            mtx_2 = mutate_matrix(mtx_1, n_cities, max_value)
            mtx_list.append(mtx_2)
            
            # 4. Calculate the shortest tour & measure the performance of Little's algorithm
            performance_2 = get_minimal_route(mtx_2)[0]
            performance_list.append(performance_2)
            
            # 5. 
            # (a) If the new performance > old performance, go to #3
            if performance_2  > performance_1:
                # new matrix becomes mtx_1, mutate from that
                mtx_1 = mtx_2.copy()
                performance_1 = performance_2
                used_or_not.append(True)
            
            # (b) If the new performance <= old performance, revert to the older matrix, then go to #3
            if performance_2 <= performance_1:
                # Don't need to do anything, just repeat with mtx_1
                used_or_not.append(False)
        
    except KeyboardInterrupt:
        pass
    
    return mtx_list, performance_list, used_or_not