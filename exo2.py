t = int(input("Please type in the temperature: "))

if(t <0):
    print("It's freezing!\nIt's cold!\nIt's cool!\nStay safe!")
elif(t>=0 and t<10):
    print("It's cold!\nIt's cool!\nStay safe!")
elif(t>=10 and t<20):
    print("It's cool!\nStay safe!")
else:
    print("Stay safe!")