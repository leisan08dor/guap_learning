PATH100000 = 'module2/practica1/data100000.txt'

x = 565124

def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i 

with open(PATH100000) as file:
    numbers = [int(line) for line in file]
    

result_index = search(numbers, x)

if result_index != -1:
    print(f" {x} - индекс {result_index}")
else:
    print('НЕ НАЙДЕН')
    
