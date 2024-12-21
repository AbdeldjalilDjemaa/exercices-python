t = [0,1,2,3,4,5]

while True:
    a = int(input("inter index between 0 and 5 (-1 to quit)"))

    if(a ==-1):
        break
    else:
        b= int(input("enter new value"))
        t[a]=b
        print(t)
