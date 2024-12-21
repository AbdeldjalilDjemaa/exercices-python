def length(lst):
    if(not lst):
        print("la liste est vide")
        return 0
    
    return len(lst)

def mean(lst):
    if(not lst):
        print("la liste est vide")
        return None

    return sum(lst)/len(lst)

def range_of_list(lst):
    if(not lst):
        print("la liste est vide")
        return None
    return max(lst) - min(lst)

liste =[1,2,3,4,5]
listev = []
print(length(liste))
print(mean(liste))
print(range_of_list(liste))

print(length(listev))
print(mean(listev))
print(range_of_list(listev))

