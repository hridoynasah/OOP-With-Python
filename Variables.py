# Switching to python 
# Ctrl + / : Single line comment ----> #
# Alt + Shift + A : Doc  String or Multi line comment ---->  """  """ 

# All Data types : 

# variable_Name = data  (Just initialize python will understhood which datatype it is)

# int type
myAge = 22  
print(myAge) 
# float type
cgpa = 3.73
print(cgpa)

# String type
Fname = "Hridoy"
Lname = "Hasan"
print(Fname)
print(Lname)

# String Concatenation
FullName = Fname + " " + Lname
print(FullName)
print("My name is" + " " + Fname + " " + Lname)

# f-string

info = f"My name is {FullName}. I am {myAge} years old. My cgpa is {cgpa}."

print(info)

# Boolean
isCoding = True
isSleeping = False

print(isCoding,isSleeping)

# data type

print(type(myAge))
print(type(info))

x = 10
y = 20

print(x + y)