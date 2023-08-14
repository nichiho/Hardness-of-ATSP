import pandas as pd
import numpy as np
import urllib.request
import json

import time
import random
import pickle

import sys
sys.path.insert(1, "..")
from littles_algorithm.algorithm import get_minimal_route

for i in range(4, 10):
    data_mtx_cities = 'data/{}'.format(i)
    
    with open(data_mtx_cities, 'rb') as f:
        mtx_cities = pickle.load(f)
    
    performance = get_minimal_route(mtx_cities)[2]
    
    file_name = 'data/{}_performance'.format(i)

    with open(file_name, 'wb') as f:
        pickle.dump(performance, f)
        
    print(i)