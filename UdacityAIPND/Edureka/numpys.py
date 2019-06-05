import numpy as np
# # ===================Creating Simple Array=================
# # 1D Array
# arr = np.array([1,2,3])
# print(arr,'\n')

# # 2D Array

# arr1 = np.array([(1,2,3),(4,5,6)])
# print(arr1)

# # Array of step Value

# # Without Step
# arr2 = np.arange(1,100)
# print(arr2)

# # With Step
# arr3 = np.arange(1,100,10)
# print(arr3)

# # Array of Zeros mXn m = rows, n = column
# arr4 = np.zeros((5,3))
# print(arr4)

# # Array of Ones
# arr5 = np.ones((2,4))
# print(arr5)

# # Array/Vector of Linear Space( Evenly Spaced Values)
# arr6 = np.linspace(0,20,5)
# print(arr6)

# Convert an existing sequence into an ndArrays
# a = [1,2,3,4,5,6,7,8,9]
# arr7 = np.asarray(a)
# print('Python Array ',a)
# print('ndarray ',arr7)

# # Restructuring a numpy Array

# arr8 = arr7.reshape((3,3))
# print("Reshape=>\n",arr8)

# # Flattening the Array RAVEL

# arr9 = arr8.ravel()
# print("Ravel=> ",arr9)

# # Indexing
# arr10 = np.arange(1,20)

# print(type(arr10[6]), arr10[6])
# print(arr10[6]+7) # Python changes int into numpy.int32 and then add the value

# # Slicing
# arr11 = np.arange(0,20,2)

# print(arr11)
# arr11_slice = arr11[4:]
# arr11_sliceOne = arr11[:9]
# arr11_sliceTwo = arr11[2:8]
# print(arr11_slice)
# print(arr11_sliceOne)
# print(arr11_sliceTwo)

# # Slice from 2D array:
# arr12 = np.array([(1,2,3),(4,5,6),(7,8,9)])
# arr12_Slice = arr12[0:2,0:3] # m = 0:2 => 2 Rows and m = 0:3 => 3 Columns
# arr12_Slice_Vector = arr12[0:3,0:1]
# print(arr12_Slice) # Now the Matrix is 2*3
# print(arr12_Slice_Vector) # This is 3*1 Vector

# # ==================Array Attributes=====================
# arr13 = np.array([(1,2,3),(4,5,6),(7,8,9)])
# print(arr13.shape) # Returns tuple Consisting of array dimesnsions
# print(arr13.ndim) # returns the number  of array dimensions ex 1D 2D 3D etc
# print(arr13.itemsize) # returns length of each element of array in bytes

# # Creating Empty array
# arr14 = np.empty([2,3],dtype=int)
# arr15 = np.empty([2,3],dtype=float)
# print(arr14)
# print(arr15)
# print(arr14.itemsize)
# print(arr15.itemsize)
# # ========================Reading for Text File===================
# arr16 = np.loadtxt('a.txt',delimiter=',')
# print(arr16)
# # ========================Reading from CSV File===================

# arr17 = np.genfromtxt('a.csv',delimiter='')
# print(arr17[1:,:])