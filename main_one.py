# import random
# import os
# import sys
# from pathlib import Path
# import time
# import matplotlib.pyplot as plt
# from sorting_algorithms import Sorting
# Path("./plots").mkdir(parents=True, exist_ok=True)

# sys.setrecursionlimit(50000)

# def sample_set(length:int, desorder:str):
#     if desorder == 'easy':
#         return random.sample(range(1,length + 10),length + 1)
    
#     if desorder == 'normal':
#         return random.sample(range(1,length * 100),length + 1)
    
#     if desorder == 'hard':
#         return sorted(list(range(1,length + 1)),reverse=True)


# shuffle = sys.argv[1]
# sample_list = [5000, 10000, 15000]

# pivot_mode = sys.argv[2] #['random', 'find_pivot', 'mean', 'median']
# plt.title('Complexidade T(n) por n - {0}'.format(pivot_mode) )

# for sample in sample_list:
#     time_complexity = 0
#     A = sample_set(sample, shuffle)
#     lb = 0
#     hb = len(A) - 1
#     start_time = time.time()
#     Sorting.quick_sort(A, lb, hb, pivot_mode)
#     time_complexity = time.time() - start_time
#     print('Execution time: {:.2f} seg'.format(time_complexity))

#     plt.plot([0, sample], [0, time_complexity], label='amostra: {0}'.format(sample))
#     plt.legend()
#     plt.savefig('./plots/{0}_{1}.png'.format(pivot_mode, shuffle))


import random
import os
import sys
from pathlib import Path
import time
import matplotlib.pyplot as plt
from sorting_algorithms import Sorting
Path("./plots").mkdir(parents=True, exist_ok=True)

sys.setrecursionlimit(50000)

def sample_set(length:int, desorder:str):
    if desorder == 'easy':
        return random.sample(range(1,length + 10),length + 1)
    
    if desorder == 'normal':
        return random.sample(range(1,length * 100),length + 1)
    
    if desorder == 'hard':
        return sorted(list(range(1,length + 1)),reverse=True)


shuffle = sys.argv[1]
sample_list = [5000, 10000, 15000]

#['random', 'find_pivot', 'mean', 'median']
pivot_mode = sys.argv[2]
plt.title('Complexidade T(n) por n - {0}'.format(pivot_mode) )

time_result = []

for sample in sample_list:
    time_complexity = 0
    A = sample_set(sample, shuffle)
    lb = 0
    hb = len(A) - 1
    start_time = time.time()
    Sorting.quick_sort(A, lb, hb, pivot_mode)
    time_complexity = time.time() - start_time
    time_result.append(time_complexity)
    print('Execution time: {:.2f} seg'.format(time_complexity))

plt.plot(time_result, sample_list, label='amostra: {0}'.format(sample))
#plt.legend()
plt.savefig('./plots/{0}_{1}.png'.format(pivot_mode, shuffle))
