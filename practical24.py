#Milan Gautam
#CS1 Batch-2
#Python Practical 24
#202103103510502

file = input("Enter Filename: ")
file = open(file, "r")
lines = file.readlines()

opr = input("Enter Number of lines to be printed: ")

for i in range(int(opr)+1):
	print(lines[i])