# # =====================Single Level Inheritance========================
# class Animal():
#     def animalName(self):
#         return "This is Parent Class and Animal Name is Tiger"
    
# class Dog(Animal):
#     def dogName(self):
#         return "This is the Child Class and Dog name is Tommy"
    
# dogObj = Dog()
# print(dogObj.animalName())
# print(dogObj.dogName())

# # =======================Multiple Inheritance===========================
# class One():
#     def displayOne(self):
#         return "Inside Method One"

# class Two():
#     def displayTwo(self):
#         return "Inside Method Two"

# class Three(Two,One):
#     pass

# obj1 = Three()
# obj2 = Three()
# print(obj1.displayOne())
# print(obj2.displayTwo())

# # =============================MultiLevel Inheritance=============================

# class One():
#     def message(self):
#         return "Method One Class One"
# class Two(One):
#     def message(self):
#         return "Method Two Class Two"

#     def display(self):
#         return self.message(), super().message() 

# class Three():
#     obj1 = Two()
#     a,b = obj1.display()
#     print(a+'\n'+b)

# Three()

# # ===============================Method Overriding ======================
# class One():
#     def __init__(self):
#         self.value = 5

#     def get_value(self):
#         return self.value
# class Two(One):
#     def get_value(self):
#         return self.value + 1

# ob1 = Two()
# print(ob1.get_value())



