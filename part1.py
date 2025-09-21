import numpy as np

def line():
    print(50*"-")

arr = [1,2,3,4,5,6] #Normal List
arr0 = np.array([1,2,3,4,5,6,7,8]) # Numpy Array
line()

ar1 = np.array([[2,3,4],[5,6,7]])
print(ar1)
line()

ar2 = np.arange(12)
print(ar2)
line()

ar3 = ar2.reshape(3,4)
print(ar3)
line()

# Row ka Column and Column ka Row
# Like A inverse Method
ar4 = ar3.T  # Transpose Method
print(ar4)
line()

# Make Flat any Matrix 
ar5 = ar4.flatten()
print(ar5)
line()

ar6 = np.random.random((3,4))
print(ar6)
line()

ar7 = ar5.ravel()
print(ar7)

line()

### Vector Matrix Tensor
vec = np.array([1,2,3])
print(vec)

line()
mat = np.array([[1,2,3],[4,5,6]])
print(mat)
line()

ten = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(ten)
line()

zero = np.zeros((3,4))
print(zero)
line()

one = np.ones((2,3))
print(one)
line()
full = np.full((3,3),9)
print(full)
line()
aran = np.arange(1,21+ 1,5)
print(aran)