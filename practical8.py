#Milan Gautam
#CS1 Batch-2
#Python Practical 8
#202103103510502

n=int(input("enter number of input: "))
list1=[]
for i in range(n):
    num=int(input("enter number: "))
    list1.append(num)
print(list1)

def minmax(list1):
    max=0
    for i in range(len(list1)):
    
      if list1[i]>max:
        max=list1[i]
    
    min=list1[0]
    for i in range(len(list1)):
        if list1[i]<min:
            min=list1[i]

    return min,max

x,y=minmax(list1)

print("minimum value is ",x)
print("maximum value is",y)