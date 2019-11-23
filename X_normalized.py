import numpy as np
#Create a random 5x5 array and store to"X"
X  = np.random.random((5,5))
#Output the original array
print("The Original Array is: ")
print(X)
print("")
#Perform Normalization with the formula and store to "Z"
Z = (X-X.mean())/(X.std())
print ("Normalized: ")
print(Z)