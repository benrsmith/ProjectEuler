fibs = []
loop = True
a = 1
b = 2
while loop == True:
    fibs.append(a)
    c = a+b
    a = b
    b = c
    if a > 4000000:
        loop = False

#def evenify(aList):
#    for num in aList:
#        if num%2 != 0:                 <- but WHY didn't this work?
#            aList.remove(num)
    
def evenify(myList):
    newList = []
    for thing in myList:
        if thing%2 == 0:
            newList.append(thing)
    return newList

fibs = evenify(fibs)
print (sum(fibs))