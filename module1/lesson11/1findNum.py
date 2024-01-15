def find_nums(n):
    assert n<=27
    nums=[]
    for i in range(1,10):
        for j in range(10):
            for k in range(10):
                if i+j+k==n:
                    num=i*10**2+j*10**1+k*10**0
                    nums.append(num)
    return nums                
print(find_nums(10))