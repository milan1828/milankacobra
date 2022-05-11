#Milan Gautam
#CS1 Batch-2
#Python Practical 6
#202103103510502

print("Calculator")
star = 148
print('''
    1)Div
    2)Mul
    3)Add
    4)Sub
    ''')
while (True):
    try:
        operator = int(input("Enter operator : "))
        break
    except ValueError and NameError:
        print("Invalid Operator\n")
while (True):
    try:
        n1 = int(input("Enter first Num : "))
        break
    except ValueError and NameError:
        print("Invalid Input\n")
while (True):
    try:
        n2 = int(input("Enter Second Num : "))
        break
    except ValueError and NameError:
        print("Invalid Input\n")

if operator == 1:
    a = n1 / n2
    print("The Quotient of the values is : ",a)
elif operator == 2:
    a = n1 * n2
    print("The Product Of The values is : ",a)
elif operator == 3:
    a = n1 + n2
    print("The Sum Of The Values is : ",a)
elif operator == 4:
    a = n1 - n2
    print("The difference between the values is : ",a)
else:
    print("Invalid Operator")