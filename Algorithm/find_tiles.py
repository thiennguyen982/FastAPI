import math as m
 
def findTiles(M, N):
    x = int(m.sqrt(4 * N + M))
    if x % 2 == 0:
        return x
    else:
        if M >= 2*x + 1:
            return x
        else:
            return x -1
        
print(findTiles(8, 0))