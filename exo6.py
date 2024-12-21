a = float(input("Please type in a price: "))

if(a>0):
    dec = int(a)
    cen = int((a-dec)*100)
    print("Dinars:",dec)
    print("Centimes:",cen)
else:
    print("ERROR")
    

        