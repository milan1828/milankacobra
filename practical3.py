#Milan Gautam
#CS1 Batch-2
#Python Practical 3
#202103103510502

n = (5,4,2,4,7,1,1)
print("tuple : ",n)

print("tuple.count() program : ",n.count(2))

print("tuple.index() program : ",n.index(2))

print("Positive tuple Indexing :",n[5])

print("Negative tuple indexing :",n[-5])

print("Slicing Tuple:",n[2:5])

n = list(n)
print("Tuple To list", n)
n[5] = 25
n = tuple(n)
print("List To Tuple :",n)
