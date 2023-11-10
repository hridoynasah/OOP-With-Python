# print("Now I need money")

# input("Give me some money : ") # It will take input only

# money = input("Give me some money : ")  # If we want to see the out put we have to strore it in a variable 
# print("Here is your money :",money)

# print(type(money))

# By default input taken from user  will be string type. 

x = input("Enter x : ")
y = input("Enter y : ")
print("Vlaue of x & y :",x,y)

sum = int(x + y)
print("Total value before typecasting : ",sum) # Output will be 100200 (Because : By default input taken from user  will be string type.)
print("Type of x before type casting : ",type(x)) # Type of x is  string

# Ei problem er solution holo type cast kora 

x_int = int(x)  # x ke type cast korlam
y_int = int(y)
print("Type of x after type casting : ",type(x_int))

print("Total value after typecasting : ",x_int + y_int) # Before : 100200 , After : 300

print()