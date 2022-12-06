import numpy as np


macierz = np.random.randint(low=0, high =1, size=(3,3))
#macierz[1:,:2]=1
#macierz[:2,0:]=1
macierz[:2,[0,2]]=1

print(macierz)
