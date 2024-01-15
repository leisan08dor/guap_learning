from collections import Counter
list = [1,4,4,6,7,7,3,2,'ф','ф','s']
def counter(list):
    cnt = Counter(list)
    dict={f'count-{key}': value for key, value in cnt.items()} 
    return dict

output = counter(list)
print(output)