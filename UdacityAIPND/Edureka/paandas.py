import pandas as pd
import numpy as np
# # Pandas Data structures
# # 1. Series
# s = pd.Series([3,-5,1,5], index = ['a','b','c','d'])
# print(s)
# print(s[0])
# print(s['c'])
# # # Creating series using ndArray
# ndarr = np.array([9,8,7,6,5,4,3,2,1])
# s1 = pd.Series(ndarr)
# print(s1)
# # # Creating using Dictionary
# dict_data = {'a':1,'b':2,'c':3,'d':4,'e':5}
# s2 = pd.Series(dict_data)
# print(s2)
# print("Index d",s2['d'])
# ndArr1 = np.array([9,8,7,6,5,4,3,2,1])
# ndArr2 = np.array(['a','b','c','d','e','f','g','h','i'])
# s3 = pd.Series(ndArr1, index = ndArr2)
# print("Pandas Series===> ")
# print(s3)
# # # Slicing
# print(s3['b':'f'])
# print(s3[1:5])

# # DataFrame data structures (2-D Data Structures)

# listOne = [9,8,7,6,5,4,3,2,1]
# tableOne = pd.DataFrame(listOne)
# print(tableOne)
# arrayTwo = np.array([(1,2,3),(4,5,6),(7,8,9)])
# tableTwo = pd.DataFrame(arrayTwo)
# print(tableTwo[2][0])

# data_dictOne = {'Ayush':pd.Series([89,91,90], index = ['Math','Chemistry','Physics']),
#                 'Amith':pd.Series([90,91,92], index = ['Math','Chemistry','Physics']),
#                 'Amar':pd.Series([55,60,70],  index = ['Math','Chemistry','Physics'])}
                
# tableThree = pd.DataFrame(data_dictOne)
# print("Table Three")
# print(tableThree)

# seriesOne = pd.Series([90,89,88], index = ['SubOne','SubTwo','SubThree'])
# seriestwo = pd.Series([88,87,86], index = ['SubOne','SubTwo','SubThree'])

# tableFour = pd.DataFrame({
#     'Ayush':seriesOne,
#     'Akshay':seriestwo
# })
# print("Before Column Addition")
# print(tableFour)

# # # Adition and Deletion of Columns
# # # Column Addition

# tableFour['Ajay'] = pd.Series([78,87,59], index = ['SubOne','SubTwo','SubThree'])
# print("After Column Addition")
# print(tableFour)

# # # Column Deletion
# poppedVal = tableFour.pop('Ajay')
# print("After Column Deletion")
# print(tableFour)
# print("Popped Value")
# print(poppedVal)
# print(tableFour.loc['SubOne'])
# # # Row Addition

# row = pd.DataFrame([[96,92],[88,86]],columns=['Ayush','Akshay'],index = ['SubFour','SubFive'])
# tableFour = tableFour.append(row)
# print(tableFour)

# # # Row Deletion

# tableFour = tableFour.drop('SubFour')
# print("After Deletion")
# print(tableFour)

# # Loading CSV Data into DataFrames
# tableFive = pd.read_csv('D:/Python/Edureka/a.csv',sep = "\t")
# print(tableFive)

# # Saving DataFrames to CSV

# seriesThree = pd.Series([91,92,93,94,90],index = ['English','Physics','Chemistry','Mathematics','Computer'])
# seriesFour = pd.Series([90,82,91,78,85],index = ['English','Physics','Chemistry','Mathematics','Computer'])
# seriesFive = pd.Series([98,82,79,82,88],index = ['English','Physics','Chemistry','Mathematics','Computer'])
# seriesSix = pd.Series([77,85,76,80,98],index = ['English','Physics','Chemistry','Mathematics','Computer'])

# tableSix = pd.DataFrame({
#     'Aamir':seriesThree,
#     'Akash':seriesFour,
#     'Aman':seriesFive,
#     'Amit': seriesSix
# })
# print("Table Six")
# print(tableSix)

# # Adding Column
# tableSix['Ayush'] = pd.Series([89,90,91,92,93], index = ['English','Physics','Chemistry','Mathematics','Computer'])
# print("Column Addition")
# print(tableSix)

# # Adding Rows
# rowOne = pd.DataFrame([[90,91,92,93,94]], columns = ['Aamir','Akash','Aman','Amit','Ayush'], index = ['Humanities'])
# tableSix = tableSix.append(rowOne)
# print("Row Addition")
# print(tableSix)

# # Saving DataFrames to CSV
# tableSix.to_csv('./a1.csv', sep='\t')
# writer = pd.ExcelWriter('./output.xlsx')
# tableSix.to_excel(writer,'Sheet')
# tableSix.to_excel('./a2.xlsx')

delivery = pd.Series([0.1,0.2,0.3,0.4,0.5,0.6,1.1,1.2,1.3,1.4,1.5,1.6,2.1,2.2,2.3,2.4,2.5,2.6,3.1,3.2,3.3,3.4,3.5,3.6])
indiaSeries = pd.Series([0,0,0,0,0,2,0,0,0,1,0,1,2,0,0,0,1,0,0,0,0,0,0,0])
ausSeries = pd.Series([0,0,0,0,0,0,0,0,2,1,0,0,1,1,1,1,0,0,2,4,1,4,0,1])
tableSeven = pd.DataFrame({
    'Delivery':delivery,
    'India':indiaSeries,
    'Australia':ausSeries
})
print(tableSeven)

tableSeven.to_excel('IndVSAus.xlsx')