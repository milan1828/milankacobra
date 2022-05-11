#Milan Gautam
#CS1 Batch-2
#Python Practical 20
#202103103510502


while(True):
	try:
		number=input("This program will throw exception and quit while entering anything other than integer: ")
		int(number)
	except ValueError:
		print("Enter a valid number, Press ctrl+c to quit the loop")
		break