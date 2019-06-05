import pandas as pd
import numpy as np
# =================================Iterating a Object===============================
# A C-style way of accessing list elements 
print("A C-style way of accessing list elements")
cars = ["Aston", "Audi", "McLaren"] 
i = 0
while(i<len(cars)):
    print(cars[i])
    i = i+1

# Accessing items using for-in loop 
print("\nAccessing items using for-in loop")
cars = ["Aston", "Audi", "McLaren"] 
for x in cars: 
	print(x) 

# Accessing items using indexes and for-in 
print("\nAccessing items using indexes and for-in")
cars = ["Aston", "Audi", "McLaren"] 
for i in range(len(cars)): 
	print(cars[i])

# Accessing items using enumerate() 
print("Accessing items using enumerate()")
cars = ["Aston" , "Audi", "McLaren "] 
for i, x in enumerate(cars,start=4): 
    print(i,x)

# ==========+++++++++++++++Iterating a DataFrame++++++++++++++===============
print("\nIterating a DataFrame Gives Column name")
N=20
df = pd.DataFrame({
   'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
   'x': np.linspace(0,stop=N-1,num=N),
   'y': np.random.rand(N),
   'C': np.random.choice(['Low','Medium','High'],N).tolist(),
   'D': np.random.normal(100, 10, size=(N)).tolist()
   })

for col in df:
   print(col)

# iteritems() => iterate over the (key,value) pairs
print("iteritems() => iterate over the (key,value) pairs")
df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
    print(key)
    print(value)

# iterrows() => iterate over the rows as (index,series) pairs
print("iterrows() = > iterate over the rows as (index,series) pairs")
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print(row_index)
   print(row)

# itertuples() => iterate over the rows as namedtuples
print("itertuples() => iterate over the rows as namedtuples")
df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print(row)
    print(row[2])