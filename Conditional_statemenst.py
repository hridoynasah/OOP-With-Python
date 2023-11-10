#in , not , not in, is, is not

# a = 5

# if a % 2 == 0 :
#     print("Even Number")
# else :
#     print("Odd Number")

x = 47

if x == 50 :
    print("Hae , 50 er Soman") #indent use korbo 
elif x < 50 :
    print("50 er choto")
    print("Koto choto ke jane")
elif x > 50 :
    print("50 er boro")
else :
    print("Hudai faltu value dise")

# Using boolean expression :

Sir = False

if Sir is True :
    print("Tel er baksho niye ashtesi sir re tel dibo")
elif Sir is not True:
    print("Sir sara kauke guni na")

# nested conditions 

boss = True

coin = "head"

if boss == True :
    print("Boss onek Joss , Beshi Beshi tel dite hobe")
    if coin != "head" :
        print("Batting korbo")
    else :
        print("Battring korbo na")
        if 10 % 2 == 0 :
            print("Dosh Jur Sonkha")
        else :
            print("Bejur sonkha")
else :
    print("Kaukei Gunar time nai amr")