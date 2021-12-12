# Iterators
#https://www.w3schools.com/python/trypython.asp?filename=demo_iterator

myTuple = ("apple","orange", "kiwi")
myit = iter(myTuple)

print(next(myit))
print(next(myit))
print(next(myit))

print()

myit = iter(myTuple)
for x in myTuple:
    print(next(myit))