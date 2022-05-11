#Milan Gautam
#CS1 Batch-2
#Python Practical 23
#202103103510502


punc = [ "!", "]", "[", ".", ",", "{", "}", "(", ")" ]
fname = input("Enter filename: ")
f = open(fname, "r")
read = f.read()
for i in punc:
	read = read.replace(i, " ")

nowords = read.split(" ")
for i in range(nowords.count("")):
	nowords.remove("")
print(nowords)
print(len(nowords))
