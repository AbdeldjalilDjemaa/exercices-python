motsuniques = set()

while True:
    mot = input("Enter a word:")
    if(mot in motsuniques):
        break
    
    motsuniques.add(mot)


print("You typed in", len(motsuniques) ,"unique words.")



