import time
import random


def bubble(array):  # Даниил
    for i_ in range(len(array)-1):
        for j_ in range(len(array)-i_-1):
            if array[j_] > array[j_+1]:
                buff = array[j_]
                array[j_] = array[j_+1]
                array[j_+1] = buff


times = dict()
for i in range(2, 7):
    times[10 ** i] = []
    for j in range(5):
        with open(f'{10 ** i}.txt', mode='r') as f:
            data = list(map(int, f.read().split('\n')))
        start = time.time()
        bubble(data)
        end = time.time()
        times[10 ** i].append(end - start)
print(times)


def comb(array):  # Олеся
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
    start_time = time.time()
    comb(numbers)
    finish_time = time.time()
    print(finish_time - start_time)


def quicksort(array):  # Никита
    if len(array) <= 1:
        return array
    base = array[len(array) // 2]
    left = [x for x in array if x < base]
    middle = [x for x in array if x == base]
    right = [x for x in array if x > base]
    return quicksort(left) + middle + quicksort(right)

# Генерация списка случайных чисел указанного размера
def random_list(size):
    return [random.randint(1, 1000) for _ in range(size)]

# Замер времени выполнения сортировки
def time_sort(array):
    start_time = time.time()
    sorted_list = quicksort(array)
    finish_time = time.time()
    return finish_time - start_time

# Размеры списков для сортировки
sizes = [100, 1000, 10000, 100000, 1000000]

# Выполнение сортировки и замер времени для каждого размера списка
for size in sizes:
    array = random_list(size)
    time_s = time_sort(array)
    print(f"Размер списка: {size}, Время сортировки: {time_s} сек.")