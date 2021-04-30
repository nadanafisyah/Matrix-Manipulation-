"""
MANIPULASI MATRIKS DENGAN NUMPY
Created by: Kelas Terbuka (https://youtu.be/rpk2_9b5TUY)
Modified by: Asisten Pemograman Geospasial 2021
Created on Fri Apr 30 2021
"""
import numpy as np

# Menampilkan Matriks
a = np.array(([6,8,5],[10,15,20]))
print('matrix a dengan ukuran:',a.shape)
print(a)

# Transpose 
print('transpose matrix dari a:')
print(a.T)

# Flatten 
print('flatten matrix a:')
print(a.ravel())

# Resize 
a.resize(3,2)
print(a)
