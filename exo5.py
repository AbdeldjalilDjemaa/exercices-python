print("Runner 1:")
n1 = input("Name: ")
t1 = float(input("Time (in seconds): "))
n2 = input("Name: ")
t2 = float(input("Time (in seconds): "))

if(t1>t2):
    print("The faster runner is "+n2)
elif(t1<t2):
    print("The faster runner is "+n1)
else:
    print (n1+" and " +n2+" have the same time")