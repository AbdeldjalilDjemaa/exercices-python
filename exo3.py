total = float(input("Total amount: "))
item = int(input("Number of items: "))
day = input("Day of the week: ")
tableday = ["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]

if(item <0):
    print("ERROR")
elif(item <5):
    if(day==tableday[0] or day==tableday[1]):
        total = total -(total*0.2)
    else:
        total = total -(total*0.1)

else:
    if(day==tableday[0] or day==tableday[1]):
        total = total -(total*0.2) -(total*0.05)
    else:
        total = total -(total*0.1) -(total*0.05)


print("Total price after discount:",total ,"dinars")