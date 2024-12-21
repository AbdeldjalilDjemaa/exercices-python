def anagrams(word1,word2):
    word1.lower()
    word2.lower()

    if(sorted(word1)==sorted(word2)):
        return True
    return False

word1 = input("enter first word:")
word2 = input("enter second word:")

print(anagrams(word1,word2))