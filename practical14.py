#Milan Gautam
#CS1 Batch-2
#Python Practical 14
#202103103510502

class employee:
    emp_name = None
    emp_age = None
    emp_city = None
    def get_data(self, name, age , city):
        self.emp_name = name
        self.emp_age =  age
        self.emp_city = city

class emp_derived(employee):
    def _init_(self, obj):
        print("Employee's Name:", obj.emp_name)
        print("Employee's Age:", obj.emp_age)
        print("Enployee's City:", obj.emp_city)

emp1 = employee()
emp1.get_data(input("Enter Employee Name: "), input("Enter Employee's Age: "), input("Enter Employee's City: "))
emp_derived(emp1)