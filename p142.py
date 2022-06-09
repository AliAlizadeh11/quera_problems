class Drug:
    def __init__(self, name, amount, price):
        self.name = name
        self.amount = amount
        self.price = price
        


class Pharmacy:
    def __init__(self, name):
            self.name = name
            self.drugs = list() 
            self.employees = list()
        
    def add_drug(self, drug):
        self.drugs.append(drug)
        
    def add_employee(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        employees_dict = {
        "first_name": self.first_name,
        "last_name": self.last_name,
        "age": self.age
        }
        
        self.employees.append(employees_dict)
        
    
    def total_value(self):
        q = 0
        for drug in self.drugs:
            result = drug.amount * drug.price
            q += result
        return q
    
    def employees_summary(self):
        l = ""
        a = 'Employees:\n'
        for i in range(len(self.employees)):
            b = f'The employee number {i+1} is {self.employees[i]["first_name"]} {self.employees[i]["last_name"]} who is {self.employees[i]["age"]} years old.\n'
            l += b
        return a + l