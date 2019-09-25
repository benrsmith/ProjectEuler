#Initial code

myList = []
for i in range(1,1001):
   myList.append(i**i)
print (str(sum(myList))[-10:])

#One liner

print (str(sum([i**i for i in range(1,1001)]))[-10:])


