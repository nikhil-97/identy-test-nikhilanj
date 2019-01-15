import numpy as np

A = np.random.randint(0,10,size=10)
B = np.random.choice([True,False],size=A.shape)

print(A[B]) #We slice the initial array "A" using "B" as mask