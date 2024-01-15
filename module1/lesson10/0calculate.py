def calculate(*num, operation='+'):  
    result=0
       
    if operation=='+':
        result=sum(num)
    elif operation=='-':
        result=num[0]
        for n in num[1:]:
           result-=n
    elif operation=='*':
        result=1
        for n in num:
            result*=n
    elif operation=='/':
        result=num[0]
        for n in num[1:]:
            result/=n
    return result
    
print(calculate(1,5,7,8))
print(calculate(5,7,8, operation='-'))
