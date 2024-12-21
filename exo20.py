liste =[]

while True:
    a = int(input("Enter a number:"))
    if(a ==0):
        break

    liste.append(a)
    print("Current list :",liste)
    liste.sort()
    print("Sorted list : ",liste)
