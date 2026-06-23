class Employee():
    def __init__(self, name,department="General", bonus=0):
        self.name=name
        self.department=department
        self.bonus=bonus
    
    def annuals_salary(self):
        salary=30000
        print("Employees Name: ", self.name)
        print("Employees dapartment: ", self.department)
        print("Salary: ", salary+self.bonus)
    
Employee_1=Employee("Moin","Engneering",bonus=1000000)
Employee_2=Employee("Navjot","Cleanig Department")
Employee_3=Employee("Farhan")

Employee_1.annuals_salary()
Employee_2.annuals_salary()
Employee_3.annuals_salary()