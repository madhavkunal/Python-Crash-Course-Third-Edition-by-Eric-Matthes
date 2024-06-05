class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary  # initialize as an integer
        
    def give_default_raise(self):
        self.annual_salary += 5000
        
    def give_custom_raise(self, custom_raise):
        self.annual_salary += custom_raise
    