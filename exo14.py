word = input("Word: ")

a = "******************************"
b = len(a)-len(word)

print(a)

print("*",end='')
i=0
while i<b//2 -1:
    print(end=' ')
    i+=1
print(word,end='')
i=b//2 + len(word)

while i<len(a)-1:
    print(end=' ')
    i+=1
print("*")

print(a)

