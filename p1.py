from typing import Iterable
def flatlist(liste):
    flat = []
    for sub in liste:
        if isinstance(sub, Iterable):
            for item in sub:
                flat.append(item)
        else:
            flat.append(sub)
    return flat

def tersfonk(liste):
    ters=[]
    t=[]
    for i in liste:
        for e in i:
            t.insert(0,e)
        ters.insert(0,t)
        t=[]
    return ters
print(flatlist([[1,'a',['cat'],2],[[[3]],'dog'],4,5]))
print(tersfonk([[1, 2], [3, 4], [5, 6, 7]]))
