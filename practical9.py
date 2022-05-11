#Milan Gautam
#CS1 Batch-2
#Python Practical 9
#202103103510502

def mul_mat():
    m=int(input("Enter the Number of Rows in a Matrix A: "))
    n=int(input("Enter the Number of the Columns of the A Matrix and the Number of the Rows of the B Matrix: "))
    p=int(input('Enter the Number of the columns of the B Matrix: '))
    A=[]
    B=[]
    C=[]   
    for x in range(m):           
        row=[]
        for y in range(n):
            row.append(int(input('Enter the A i=%d, j=%d element:'%(x,y))))
        A.append(row) 
    print('Now Taking Input For matrix B..........\n\n')
    for q in range(n):    
        row=[]
        for s in range(p):
            row.append(int(input('Enter the B i=%d, j=%d element:'%(q,s))))
        B.append(row)
   
    for i in range(m):    
        row=[]
        for j in range(p):
            c=0
            for k in range(n):
                tmp=A[i][k]*B[k][j]
                c=c+tmp
            row.append(c)
        C.append(row)
   
    return C


def entry(p):
    m=int(input("Enter the Number of Rows in a Matrix A and the Number of the Rows of the B Matrix: "))
   
    n=int(input("Enter the Number of the Columns of the A Matrix and the Number of the Columns of the B Matrix: "))
    A=[]
    B=[]   
   
    for x in range(m):           
        row=[]
        for y in range(n):
            row.append(int(input('Enter the A i=%d, j=%d element:'%(x,y))))
        A.append(row)  
    for x in range(m):            
        row=[]
        for y in range(n):
            row.append(int(input('Enter the B i=%d, j=%d element:'%(x,y))))
        B.append(row) 
    return add_sub(A,B,m,n,p)
       
def transpose():
    m=int(input("Enter the Number of Rows in a Matrix A: "))
   
    n=int(input("Enter the Number of the Columns of the A Matrix: "))
    A=[] 
    for x in range(m):            
        row=[]
        for y in range(n):
            row.append(int(input('Enter the A i=%d, j=%d element:'%(x,y))))
        A.append(row) 
    for i in range(n):
        row=[]
        for j in range(m):
            row.append(A[j][i])
        B.append(row)    
    return B


def add_sub(A,B,m,n,p):
    C=[]
    for i in range(m):
        row=[]
        for j in range(n):
            if p==1:
                row.append(A[i][j]+B[i][j])
            elif p==2:
                row.append(A[i][j]-B[i][j])
        C.append(row)
    return C

def mat_out(A):
    for x in range(len(A)):
        print('|', end='')
        for y in range(len(A[x])):
            if y<=(len(A[x])-2):
                if A[x][y]>9:
                    print(A[x][y],"   ",end="")
                else:
                    print(A[x][y],"  ",end="")
                    
            else:
                print(A[x][y],end="")
        print('|')    
 
choice=int(input("Enter the following choice:\n1. Press 1 for Matrix Addition\n2. Press 2 for Matrix Subtraction\n3. Press 3 for Matrix Multiplication\n4. Press 4 for Transpose of a Matrix\nEnter Here: "))
if choice==1:
    A=entry(1)
    print('The Addition of Matrix is : ')
    mat_out(A)
if choice==2:
    A=entry(2)
    print('The Subtraction of the Matrix : ')
    mat_out(A)
if choice==3:
    A=mul_mat()
    print('The Multiplication of the matrix :')
    mat_out(A)
if choice==4:
    A=transpose()
    print('The Transpose of the of the Matrix :')
    mat_out(A)