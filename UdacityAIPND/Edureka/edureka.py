# # ======================Command Line Paramaters====================
# import sys
# print(str)
# print(sys.argv)
# print(len(sys.argv))

# # ========================Sequence and File Operations=====================
# str = input("Enter your name")
#print(str)

# # ========================Python File Operations=========================
#import os
# newFile = open('a.txt','a')
# for i in range(0,10):
#     newFile.write('\n I am not Happy')

# print(newFile.mode)
# print(newFile.name)
# os.rename('a.txt','a1.txt')

# # =========================Sequences=======================================

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# print(len(list))
# # List Slicing
# print(list[-8::1])
# # Repetition
# print(list * 2)
# # Concatination
# print(list + list1)
# # Membership Testing
# print(25 in list)
# # POP
# a = list.pop(3)
# print(list, "\nPopped Value", a)
# # Remove
# a = list.remove(9)
# print(list, "\nRemoved Value", a)
# # Append
# list.append(9)
# print(list, "\n9 Appended")
# # Insert
# list.insert(3,4)
# print("List Insert ",list)
# # Extend
# list.extend([10,11,12])
# print("List Extend ",list)
# # Tuple Inside a List
# list2 = [(1,2,"Tuple0"),(3,4,"Tuple1")]
# print(list2[0][2:3:1])
# # Method 1
# list3 = [x**2 for x in [1,2,3,4,5]]
# print(list3)
# # Method 2
# list3 = []
# for x in range(1,6):
#     list3.append(x**2)
# print(list3)

# # ==========================Sets==========================================
# x = set((1,2,1,3,"India is a good Country"))
# print(x)
# #You cannot access items in sets by referring to index.One way of accessing it is

# list4 = [1,2,3,4,2,1,5,3,"India","China","Indonesia","India"]
# x = set(list4)

# list4 = list(x)
# print(list4)
# # ==OR==
# list4 = []
# for i in x:
#     list4.append(i)
# print(list4)

# # You cannot change items of set. but you can add items

# thisSet = {"Ayush", "Kumar"}
# thisSet.add("Sinha")
# print(thisSet)

# # Update
# thisSet1 = {"Ayush", "Sinha"}
# thisSet1.update({"Akshay","Sinha"})
# print(thisSet1)
# # # Length
# print(len(thisSet1))
# # # Remove/Discard  Remove raise erro if item not found but discard doesn't
# thisSet1.remove("Sinha")
# print(thisSet1)
# thisSet1.add("Sinha")
# print(thisSet1)
# thisSet1.discard("Sinha")
# print(thisSet1)
# # # pop will remove last item
# x = thisSet1.pop()
# print(x)
# print(thisSet1)
# # # clear() method empties the set
# thisSet1.clear()
# print("After Cleaning",thisSet1)
# # # del() method deletes the list
# del thisSet1
# print(thisSet1)
# # Union
# setOne = {1,2,3,4,5}
# setTwo = {4,5,6,7,8}
# union = setOne | setTwo
# print("Union ",union)
# # # Intersection
# intersection = setOne & setTwo
# print("Intersection ",intersection)
# # # Difference
# difference1 = setOne - setTwo
# difference2 = setTwo - setOne
# print("Difference1 ",difference1)
# print("Difference2 ",difference2)
# # # Subset and Superset
# setThree = {1,2,3,4,'a','b','c','d'}
# setFour = {1,2,'a','b'}
# print("Subset=> ",setFour.issubset(setThree))
# print("SuperSet=> ",setThree.issuperset(setFour))

# # =====Important Built in Functions=======

# grocery = ['Bread','Butter','Vegetables','Fruits']
# enumerateGrocery = list(enumerate(grocery))
# enumerateGroceryInedx = list(enumerate(grocery,10))
# print("Enumerate 0",enumerateGrocery,"\nEnumerate 10",enumerateGroceryInedx)
# # ===Lambda Functions===
# ans = (lambda a,b: (a*b)**2)
# print(ans(2,3))
# # ===Map===
# def square (val):
#     return val**2

# listSix = [1,2,3,4,5,6,7,8,9]
# squared = list(map(square,listSix))
# print(squared)
# # # Map with Lambda
# squared = list(map(lambda x:x**2,listSix))
# print(squared)
# # ===Filter===
# def even (x):
#     if(x % 2 == 0):
#         return True
#     else:
#         return False
# listSeven = [1,2,3,4,5,6,7,8]
# evenNos = list(filter(even,listSeven))
# print("Normal Function=> ",evenNos)

## filter with Lambda
# evenNos = list(filter(lambda z: True if z%2 == 0 else False,listSeven))
# print("Lambda Function=> ",evenNos)
# # ===================Function=======================
# def funcSum(a,b,c,d):
#     sum = a**b + c*d
#     return sum
# print(funcSum(d=3,b=2,c=4,a=5))
# def sumFunc(a,b,c,d=4):
#     sum = a**b + c+d
#     return sum

# print(sumFunc(3,4,5))
# print(sumFunc(3,4,5,6))

# #=====================OOPS=================================
# class Edureka:
#     def __init__(self):
#         self.__pri = ("I am Private")
#         self._pro = ("I am Protected")
#         self.pub = ("I am Public")

# ed = Edureka()
# print(ed.pub)
# print(ed._pro)
# print(ed.__pri) # Private attributes cannot be accessed from outside class
# # Python performs name mangling of private variables. Every member with double underscore will be changed to _object._class__variable. If so required, it can still be accessed from outside the class, but the practice should be refrained.

# class Profile:
#     def __init__(self,name,std,roll):
#         self.name = name
#         self.std = std
#         self.roll = roll

#     def getProfile(self):
#         print("You have given your name as %s, Your Class is %d, and Your Roll No is %d" %(self.name,self.std,self.roll))

# class Profile1:
#     def getProfile(self):
#         print("You have given your name as %s, Your Class is %d, and Your Roll No is %d" %(self.name,self.std,self.roll))

# ob1 = Profile("Ayush",4,10)

# ob2 = Profile1()
# ob2.name = "Ayush"
# ob2.std = 5
# ob2.roll = 10

# ob1.getProfile()
# ob2.getProfile()

# class Name():

#     def getName(self):
#         name = 'Ayush'
#         return name

#     def __getAddress(self):
#         address = 'Bengaluru'
#         return address

# ob1 = Name()
# print(ob1.getName())
# # # Accessing Private Method
# # print(ob1.__getAddress())  # Private Methoda and Attributes cannot be accessed Directly
# print(ob1._Name__getAddress()) # Accessing Private Variable/Method object._className__variableName/methodName


# # Method Overloading in Python
# class MultipleConstructor():
#     # def __init__(self, length, breadth):
#     #     self.length = length
#     #     self.breadth = breadth

#     # @classmethod
#     # def customConstructor(cls, length, breadth, height):
#     #     cls.length = length
#     #     cls.breadth = breadth
#     #     cls.height = height

#     def area(self, length, breadth, height = None):
#         if height is None:
#             return length * breadth
#         else:
#             return length * breadth * height
        


# class CheckConstructor():
#     square = MultipleConstructor()
#     cuboid = MultipleConstructor()
#     print("Without Overloading=> ",square.area(5, 6))
#     print("With Overloading=> ",cuboid.area(3, 4, 5))


