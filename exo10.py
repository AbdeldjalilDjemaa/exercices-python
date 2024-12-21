word = input("Word: ")
i=0
n = len(word)
while i < n/2:
    if(word[i]!=word[n-i-1]):
        print("No, it's not a palindrome.")
        break
    i+=1
else:
        print("Yes, it's not a palindrome.")