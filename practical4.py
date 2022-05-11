#Milan Gautam
#CS1 Batch-2
#Python Practical 54
#202103103510502

dict = {
    "brand": "MARUTI",
    "model": "800",
    "year": 2006
}

dict2 = {
    "batch no.": "MAr8oo"
}
dict.update(dict2)
print("Updated Dictionary :",dict)

dict.pop("model")
print("Element Removed :",dict)

dict2.clear()
print("dictionary 2 cleared :",dict2)
dict3 = dict.copy()
print("Third Dictionary :",dict3)
print("get() function :",dict.get("year"))
print("items() function :",dict.items())
print("keys() function :",dict.keys())
dict.popitem()
print("popitem() function :",dict)