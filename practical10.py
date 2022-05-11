#Milan Gautam
#CS1 Batch-2
#Python Practical 10
#202103103510502

def add(a):
   
    sum=0
    for x in a:
        sum=sum+x
    return sum   

 
def sub(a,b):
    return a-b
def mul(a):
    ans=1
    for x in a:
        ans=ans*x
    return ans
def div(a,b):
    return(a/b)
def odev(a):
    if(a%2==0):
        return 1
    else:
        return 0

def entry(len, choice):
    list=[]
    total=0
    for x in range(len):
        list.append(int(input("enter a number: ")))
    
    if(choice==1):
        total=add(list)
    if(choice==2):
        total=mul(list)
    return total

print('''Following are the choices:
Enter 1 for Addition 
Enter 2 for Multiplication 
Enter 3 for Substraction 
Enter 4 for division 
Enter 5 for Odd/Even ''')

choice=int(input("Enter Your Choice: "))
if(choice==1 or choice == 2):
    len=int(input("Enter the number of the entity: "))
    if(choice==1):
        print("the Addition of the %d numbers are = %d"%(len,entry(len,choice)))
    else:
        print("the multiplication of the %d numbers are = %d"%(len,entry(len,choice)))
if(choice==3):
    a=int(input("Enter a number"))
    b=int(input("Enter a numner"))
    print("%d-%d=%d"%(a,b,sub(a,b)))
if(choice==4):
    a=int(input("Enter a number"))
    b=int(input("Enter a numner"))
    print("%d/%d=%d"%(a,b,div(a,b)))
if(choice==5):
    a=int(input("Enter a number"))
    if(odev(a)==1):
        print(a, "is the Even number")
    else:
        print(a, "is the Odd number")

 