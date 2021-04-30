"""
INVERSE DAN DETERMINAN MATRIKS DENGAN NUMPY
Created by: Kelas Terbuka (https://youtu.be/gMQwec7NBVY)
Modified by: Asisten Pemograman Geospasial 2021
Created on Fri Apr 30 2021
"""
import numpy as np

# Menampilkan matriks ordo 2x2
a = np.array(([1,-1],[1,1]))
print (a)

# Inverse matriks ordo 2x2
a_inv = np.linalg.inv(a)
print(a_inv)

# Menampilkan matriks ordo 3x3
b = np.array(([3,1,0],[2,1,1],[6,2,2]))
print (b)

# Invers matriks ordo 3x3
b_inv = np.linalg.inv(b)
print(b_inv)

# Determinan matriks ordo 2x2
det_a = np.linalg.det(a)
print(det_a)

# Determinan matriks ordo 3x3
det_b = np.linalg.det(b)
print(det_b)

