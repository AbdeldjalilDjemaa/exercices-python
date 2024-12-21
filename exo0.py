a =int(input("How many people need a ride "))
b =int(input("How many people fit in one taxi "))

if(a%b == 0):
    c = a//b
else:
    c = a//b +1
print("Number of taxis needed:", c) 
