def find_max(l):
    if len(l)>1:
        max_ = find_max(l[1:])
        if l[0]<max_:
            return max_
        else:
            return l[0]
    if len(l)==1: 
        return l[0] 
l=[-1,-125125,2151261,0,125215166,-1521267888]
print(find_max(l))