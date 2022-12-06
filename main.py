import numpy as np

list = []
for i in range(7,-1,-1):
    c = 2 ** i
    list.append(c)
print(list)
list =[2**i for i in range(7,-1,-1)]
print(list)

wagi = np.array(list)
print(wagi)

liczba_bin = np.random.randint(low=0, high =2, size=(8))
print(liczba_bin)
wynik = liczba_bin * wagi
print(wynik)
liczba_dzies = wynik.sum()
print(liczba_dzies)