def add(a):
    b=[]
    while a>0:
        b.append(a%10)
        a=a//10
    b.reverse()
    return b
def create_full_sorted_list(l):
    l.sort(reverse=True)
    return list(map(add,l))

nums=[86,85,90,7,91]
nums=create_full_sorted_list(nums)