import numpy as np

arr = np.random.randint(low=0,high=100,size=10)
print("Initial array = ",arr)
arr[1::2] = -10 #arr[1::2] chooses alternate indices, starting from index 1
print("Array after setting alternate elements to -10",arr)