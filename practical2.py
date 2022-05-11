#Milan Gautam
#CS1 Batch-2
#Python Practical 2
#202103103510502

lst = [1,2,3,4,5,6,7]
print(lst)

print("append()")
lst.append(8)  
print(lst)

print("extend()")
lst2 = [9,10]
print(lst2)
lst.extend(lst2)   
print(lst)

print("insert()")
lst.insert(0,0)     
print(lst)

print("remove()")
lst.remove(10)      
print(lst)

print("clear()")
lst2.clear()         
print(lst2)

print("index()")
print(lst.index(5))         

print("count()")
print(lst.count(3))         

print("sort()")
lst.sort()      
print(lst)

print("reverse()")
lst.reverse()      
print(lst)

print("copy()")
lst3 = lst.copy()
print(lst3)

print()
print()

large_lst = [5,356,74,8834,24,83]

print("Positive Indexing")
for i in range(len(large_lst)):
    print(large_lst[i])

print("Negative Indexing")
count = len(large_lst) - 1
while count >= 0:
    print(large_lst[count])
    count-=1

print("Slicing")
print(large_lst[2:5])

print("Append on list element")
large_lst[0] = 43434
print(large_lst)

print("Remove One Element From The List")
large_lst.pop(3)
print(large_lst)

print("Remove More Than One Elements From The List")
del(large_lst[3:5])
print(large_lst)