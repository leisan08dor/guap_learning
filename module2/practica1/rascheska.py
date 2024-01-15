import random
import time

def comb(array):
    gap = len(array)
    swaps = True
    while gap > 1 or swaps:
        gap = int(gap // 1.25)  
        swaps = False
        for i in range(len(array) - gap):
            j = i + gap
            if array[i] > array[j]:
                array[i], array[j] = array[j], array[i]
                swaps = True
                
sizes = [100, 1000, 10000, 1000000]
for size in sizes:
    numbers = random.sample(range(size), size)
    start_time=time.time()
    result_index = comb(numbers)
    finish_time=time.time()
    print(finish_time-start_time)