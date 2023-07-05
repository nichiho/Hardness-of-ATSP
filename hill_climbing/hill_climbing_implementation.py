# Imports

from hill_climbing import hill_climbing_open_file, hill_climbing_continue
import numpy as np

import os

import pickle

# Open data
n_runs = 10
n_cities = 30
max_value = 10000
n_generations = 1500
folder = 'data'

mtx_list, run_time_list, performance_list, used_or_not_list, indices_list = hill_climbing_open_file(n_runs, n_cities, max_value, n_generations, folder)

# Continue running hill-climber
mtx_list_continued, run_time_list_continued, performance_list_continued, used_or_not_continued, indices_continued = hill_climbing_continue(n_cities, max_value, 500, mtx_list[2], run_time_list[2], performance_list[2], used_or_not_list[2], indices_list[2])

# Save the lists
data = {'mtx_list': mtx_list,
        'run_time_list': run_time_list,
        'performance_list': performance_list,
        'used_or_not_list': used_or_not_list,
        'indices_list': indices_list}

n_generations = 1500

filename = 'data/list_{}_{}_{}_{}.pkl'.format(n_runs, n_cities, max_value, n_generations)

with open(filename, 'wb') as f:
    pickle.dump(data, f)