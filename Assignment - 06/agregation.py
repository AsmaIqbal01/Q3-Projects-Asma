class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee  # Aggregation: reference to an existing Employee object

    def show_employee(self):
        print(f"Department: {self.dept_name}")
        self.employee.display()

# Example usage:
if __name__ == "__main__":
    emp = Employee("Jane Doe", "Developer")  # Employee exists independently
    dept = Department("IT", emp)              # Department references the Employee

    dept.show_employee()  # Output shows department along with employee details

    # The Employee object still exists independently:
    print(f"Access employee directly: {emp.name}, {emp.position}")
