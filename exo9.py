tablecity =[]
i=0

while True:
    city = input("city: ")
    if(city =="stop"):
        break
    tablecity.append(city)
    i+=1

for i in range(len(tablecity)):
    for j in range(len(tablecity)-1):
        if len(tablecity[j]) < len(tablecity[j+1]):
            a= tablecity[j]
            tablecity[j] = tablecity[j+1]
            tablecity[j+1] =a

for i in range(len(tablecity)):
    b = len(tablecity[i])*1000000
    print(tablecity[i] +" population: ",b)

