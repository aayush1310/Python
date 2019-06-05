import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# # Number of Dimension od Data Structures

# # 1D
data_frameOne = pd.Series(np.arange(1,50,2))
print(data_frameOne.ndim)
# # 2D
seriesOne = pd.Series(np.arange(1,75,3))
seriesTwo = pd.Series(np.arange(1,50,2))
seriesThree = pd.Series(np.arange(1,30,1))
data_frameTwo = pd.DataFrame({
    'One':seriesOne,
    'Two':seriesTwo,
    'Three':seriesThree
})
print(data_frameTwo)
print("Size",data_frameTwo.ndim)

# # Axes() Returns list of Axes of the row  Labels

print("Axes",data_frameTwo.axes)

# # Values gives values n Array
print(data_frameTwo.values)
print(data_frameTwo.values[2])

# # Head Gives First Five Rows by Default

print(data_frameTwo.head())
print(data_frameTwo.head(n=10))

# # Tail Gives Last Five Rows

print(data_frameTwo.tail())
print(data_frameTwo.tail(8))

# # Dictionary to DataFrame

dictionarys = {
    'even':np.arange(0,100,2),
    'odd':np.arange(1,100,2)
}
data_frameThree = pd.DataFrame(dictionarys)

print(data_frameThree)

# # SUM
print("Sum")
print(data_frameThree.sum())

# # Standard Deviation
print("Standard Deviation")
print(data_frameThree.std())

# # Aggreagated Functions ==> Aggregated Functions Returns Single Aggregated valued for each group
print("Aggregation==>")
print(data_frameThree.groupby('odd').groups)

# # Iterating DataFrame ####Iteritems####Iterates over each column as key value pair

for key, value in data_frameTwo.iteritems():
    print(key)
    print(value)

# # Iterates over each row as key,value pair

print('\n')
for key,value in data_frameTwo.iterrows():
    print(key)
    print(value)

# # =========Group By==========
world_cup = {
    'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
    'Rank':[7,7,2,1,6,4,1,2,1,2,1],
    'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]
}
data_frameFour = pd.DataFrame(world_cup)
print(data_frameFour.groupby(['Team','Rank']).groups)

for name,group in data_frameFour.groupby(['Team','Rank']):  # Here Team name is Key and value is Group By Objects.
    print(group)
    print("================================")
    print(name)
    print("================================")

# # Getting Group Values
grouped = data_frameFour.groupby('Team')
print(grouped.get_group('Australia'))
print("================================")
groupedOne = data_frameFour.groupby(['Team','Rank'])
print(groupedOne.get_group(('Australia',1)))
print("================================")
print(groupedOne.get_group(('Australia',2)))

# # Concatination ==> Conacatinating Two or more data Structures

winners = {
    'Team':['West Indies','West Indies','India','Australia','Pakistan','Sri Lanka','Australia','Australia','Australia','India','Australia'],
    'Rank':[7,7,2,1,6,4,1,2,1,2,1],
    'Year':[1975,1979,1983,1987,1992,1996,1999,2003,2007,2011,2015]
}
chokers = {
    'Team': ['South Africa','New Zealand', 'Zimbabwe'],
    'Rank':[1,5,9],
    'Points':[895,764,656]
}
dataFrame_winners = pd.DataFrame(winners)
dataFrame_chokers = pd.DataFrame(chokers)
print("====Concatination==== Default Axis = 0")
print(pd.concat([dataFrame_winners,dataFrame_chokers]))

print("Concatinate Across Axis = 1")
print(pd.concat([dataFrame_winners,dataFrame_chokers], axis= 1))

# # DataFrame can also be Appended
print("====Winners Append Chokers====\n")
print(dataFrame_winners.append(dataFrame_chokers))

print("====Chokers Append Winners====\n")
print(dataFrame_chokers.append(dataFrame_winners))

# # Merging and Joining===> Array must be of same length
left = pd.DataFrame({
    'key':['K0','K1','K2','K3','K4','K5'],
    'A': ['A0','A1','A2','A3','A4','A5'],
    'B': ['B0','B1','B2','B3','B4','B5']
})
right = pd.DataFrame({
    'key':['K0','K1','K2','K3','K4'],
    'C': ['C0','C1','C2','C3','C4'],
    'D': ['D0','D1','D2','D3','D4']
})
print("====Merge====\n")
print(pd.merge(left,right,on='key'))

# Left Join
print("====Left Join====\n")
print(pd.merge(left,right,on='key',how='left'))

# Right Join
print("====Right Join====\n")
print(pd.merge(left,right,on='key',how='right'))

# Outer Join
print("====Outer Join====\n")
print(pd.merge(left,right,on='key',how='outer'))

# Inner Join
print("====Inner Join====\n")
print(pd.merge(left,right,on='key',how='inner'))