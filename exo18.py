numbers =[1,2,3,4,5]
print("Tableau initiale",numbers)
while True:
    a = int(input("Menu \n 1.Append \n 2.Insert \n 3.Pop \n 4.Remove \n 5.Quit\n"))

    if(a==1):
        b= int(input("Enter value"))
        numbers.append(b)
        print(numbers)
    elif(a==2):
        b= int(input("Enter value"))
        i = int(input("Enter index"))
        numbers.insert(i,b)
        print(numbers)
    elif(a==3):
        numbers.pop()
        print(numbers)
    elif(a==4):
        b=int(input("Enter number"))
        numbers.remove(b)
        print(numbers)
    else:
        break

print(numbers)