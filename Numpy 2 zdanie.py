"""Zadanie 2.
• Utwórz losową macierz o wymiarach 5x5. Znajdź największy i najmniejszy element. (patrz tab4_2d;
metoda max(), min())
• Wypisz największe elementy w każdym z wierszy (axis = 1) i w każdej z kolumn (axis = 0).
• Policz sumę wartości w poszczególnych wierszach.
"""
import numpy as np


macierz = np.random.randint(low=0, high =25, size=(5,5))
print("Max : ",macierz.max())
print("min",macierz.min())
print("Max wartość w wierszu : ",macierz.max(axis=1))
print("Minimalna wartość w wierszu",macierz.min(axis=1))
print("Max wartość w kolumnie : ",macierz.max(axis=0))
print("Minimalna wartość w kolumnie",macierz.min(axis=0))
print(macierz)
print("Suma kolumny",macierz.sum(axis=0))

print("wycinek",macierz.arr)

