#Milan Gautam
#CS1 Batch-2
#Python Practical 26
#202103103510502


src = input("Name of source file: ")
des = input("Name of destination file: ")

src_op = open(src, "r")
des_op = open(des, "r")

des_op.write(src.read())

src_op.close()
des_op.close()
print("Operation Successful !")