import random
import sys
import time
import matplotlib.pyplot as plt
from sorting_algorithms import Sorting

sys.setrecursionlimit(50000)

def sample_set(length:int, desorder:str):
    if desorder == 'easy':
        return random.sample(range(1,length + 10),length + 1)
    
    if desorder == 'normal':
        return random.sample(range(1,length * 100),length + 1)
    
    if desorder == 'hard':
        return sorted(list(range(1,length + 1)),reverse=True)

SAMPLE_SHUFFLE = ['easy', 'normal', 'hard'] 
SAMPLE_LENGTH = [1000,2000,5000]
PIVOT_TYPE = ['random', 'find_pivot', 'mean', 'median']
RESULT = {}

plt.title('Complexidade T(n) por n')

for pivot_type in PIVOT_TYPE:
    time_complexity = []
    i = 0
    for sample_length in SAMPLE_LENGTH:
        sample = sample_set(sample_length,SAMPLE_SHUFFLE[i])
        lb = 0
        hb = len(sample) - 1
        start_time = time.time()
        Sorting.quick_sort(sample, lb, hb, pivot_type)
        print('sample shuffle: {0} case, pivot type: {1}, sample length: {2}'.format(SAMPLE_SHUFFLE[i], pivot_type, sample_length))
        total_time = time.time() - start_time
        print('Execution time: {:.2f} seg'.format(total_time))
        time_complexity.append(total_time)
        i += 1

    plt.plot(SAMPLE_LENGTH, time_complexity, label='pivoteamento: {0}'.format(pivot_type))
    plt.legend()
    plt.savefig('./plots/{0}.png'.format(pivot_type))