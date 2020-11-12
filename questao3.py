import numpy as np 

mat=np.empty((10,10))
for i in range(10):
    for j in range(10):
        mat[i][j]= input("Digite um numero:\n")

print (mat)