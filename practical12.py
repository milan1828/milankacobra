#Milan Gautam
#CS1 Batch-2
#Python Practical 12
#202103103510502

class student:
    std_name = None
    std_age = None
    std_branch = None
    std_city = None
    def get_data(self, name, age, branch, city):
        self.std_name = name
        self.std_age = age
        self.std_branch = branch
        self.std_city = city
    def display(self):
        print("Name:", self.std_name, "\nAge:", self.std_age, "\nBranch:", self.std_branch, "\nCity:", self.std_city)
        
std_obj = student()
std_obj.get_data("Milan Gautam", "18", "B.tech CSE", "Vapi")
std_obj.display()