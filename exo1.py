name = input("Please enter your name: ")

if(name == "VIP"):
    print("Enjoy the show for free!")
else:
    t = int(input("How many tickets would you like to buy? "))
    s = t*15.50
    print("The total cost is",s)
    print("Enjoy your tickets!")