# Imports

from hill_climbing import hill_climbing_open_file, hill_climbing_continue

import os

import pickle

n_runs = 10
n_cities = 30
max_value = 10000
n_generations = 1500
folder = 'data'

# Continue running hill-climber
for i in range(0, 5):
        
        # Open first batch of data
        mtx_list, run_time_list, performance_list, used_or_not_list, indices_list = hill_climbing_open_file(n_runs, n_cities, max_value, '1500_2', folder)
        
        hill_climbing_continue(n_cities, max_value, 300, mtx_list[i], run_time_list[i], performance_list[i], used_or_not_list[i], indices_list[i])

        # Save the lists
        data = {'mtx_list': mtx_list,
                'run_time_list': run_time_list,
                'performance_list': performance_list,
                'used_or_not_list': used_or_not_list,
                'indices_list': indices_list}

        filename = 'data/list_{}_{}_{}_{}.pkl'.format(n_runs, n_cities, max_value, '1500_2')

        with open(filename, 'wb') as f:
                pickle.dump(data, f)