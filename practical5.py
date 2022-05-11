#Milan Gautam
#CS1 Batch-2
#Python Practical 5
#202103103510502

str = "My name is milan "

print("lower() :",str.lower())

print("upper() :",str.upper())

print("split() :",str.split())

str2 = "".join(str)
print("find() :",str2.find("milan"))

nstr = "nasa goes to moon"
print("string before: ",nstr)
rstr = nstr.replace("nasa", "isro")
print("new string: ",rstr)