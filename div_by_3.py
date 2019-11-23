import numpy as np
#Create an array ranging from 1-100
x = np.array(range(1,101))
#Resize array to 10x10
x.resize(10,10)
#Square each element and store to "z"
z = x*x
print(z)
print("")
print("The elements divisible by 3 are: ") 
#Elements divisible by 3
q = z[z%3 == 0]
#Print elements divisible by 3
print(q)