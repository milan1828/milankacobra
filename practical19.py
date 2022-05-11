#Milan Gautam
#CS1 Batch-2
#Python Practical 19
#202103103510502

class base:
    def display(self):
        print("i am base class")

class derive(base):
    def display(self):
        print("i am derive class")
        super().display()

ob=derive()
ob.display()
