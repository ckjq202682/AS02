# AS02

mylist = [1, 2, 3]
search = int(input("Input value"))

def searchlist(mylist, search):
    for i in range(len(mylist)):
        if mylist[i] == search:
            return "FOUND"
    return "NOT FOUND"

print(searchlist(mylist, search))
