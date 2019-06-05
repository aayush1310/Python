import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # By Default plots on Y-Axis 
# plt.plot([1,2,3,4,10])
# plt.show()

# # Both Y and X Axis ********plt.plot(X-Axis,Y-Axis)**********
# y_values = [1,2,3,4,5,6,7,8,9]
# x_values = [2,4,6,8,10,12,14,16,18]

# plt.plot(x_values,y_values)
# plt.show()

# # Exponential Graph y = x^2

# x_values = np.arange(0,10,0.1)

# plt.plot(x_values,[i**2 for i in x_values])
# plt.show()

# # Multiline plots(Multiple Line in same plots)==Here it will be y = x^2, y = x^3 and y = x^4

# x_values = np.arange(0,10,1)


# plt.show()

# In One plot
# x_values = np.arange(0,10,1)
# # plt.plot(x_values,[i**2 for i in x_values],x_values,[i**3 for i in x_values],x_values,[i**4 for i in x_values])
# plt.plot(x_values,[i**2 for i in x_values],label = "Square")
# plt.plot(x_values,[i**3 for i in x_values], label = "Cube")
# plt.plot(x_values,[i**4 for i in x_values], label = "Power 4")
# plt.legend()
# plt.grid()
# # Limiting the Axis (Scale of the plot can be set using axis())
# plt.axis([0,3,0,3])
# # Limiting can be done using X-Lim and Y-Lim
# plt.xlim(0,3)
# plt.ylim(0,3)
# # Adding Title 
# plt.title("Sample Graphs")
# # Adding X-Label and Y-Label
# plt.xlabel("X-Axis")
# plt.ylabel("Y-Axis") 
# # Saving in a File
# plt.savefig('matplot.png') 
# plt.show()

# # Plot Types
# # Histogram (Displays info of variable over a range of frequences)
# readIndVsAus = pd.read_excel('IndVSAus.xlsx')
# score_India = readIndVsAus['India']
# score_Aus = readIndVsAus['Australia']
# plt.hist([score_India,score_Aus], color=['blue','yellow'])
# legend = ['India','Australia']
# plt.legend(legend)
# plt.grid()
# plt.title('India Vs Australia in World Cup 2019')
# plt.xlabel('Runs/Delivery')
# plt.ylabel('Frequency')
# # # Till here the graph displays data in decimal format
# plt.xticks(range(0,7))
# plt.yticks(range(1,20))
# plt.show()

# # Bar Graph
# movies = pd.read_excel('MoviesData.xlsx')
# label = movies['Label']
# no_of_movies = movies['No_of_movies']
# # With Overlapping X Axis Values
# plt.bar(label,no_of_movies)
# plt.grid()
# # Without Overlapping X Axis Values
# fig, ax1 = plt.subplots() 
# ax1.bar(label,no_of_movies)
# fig.autofmt_xdate()
# plt.show()
# # Plotting a Dictionary using Bar Graph
# dictionarys = {'A':30,'B':20,'C':28,'D':45}

# for i , key in enumerate(dictionarys):
#     plt.bar(i,dictionarys[key])

# plt.show()

# # enumerate(iterable,start = 0)iterable = any object support iteration, start= the index value to start
# word = 'Happy'

# for i,j in enumerate(word):
#     print(i,'===========',j)
# print('================================')
# for i,j in enumerate(word,2):
#     print(i,'===========',j)

# # Pie Chart
# plt.figure(figsize=(3,3))
# x= [40,26,6]
# labels = ['C','C++','Java']
# plt.pie(x, labels= labels)
# plt.show()

# # Scatter Plot
# x = np.random.rand(200)
# y = np.random.rand(200)

# print(x,y)
# plt.scatter(x,y)
# plt.show()
