import time
import random

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