import numpy as np

a = np.random.randint(low=1,high=100,size=(5,4))
print("Initial random array = ",a)
a[a>50] = 100
print("Array after setting elements >50 to 100 = ",a)