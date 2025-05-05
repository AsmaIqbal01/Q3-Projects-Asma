class Employee:
    def __init__(self,name,salary,ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn


if __name__ == "__main__":
    emp=Employee("John Doe",50000,"123-45-6789")

    print("Name : ",emp.name)

    print("Salary : ",emp._salary)
    try:
        print("SSN : ", emp.__ssn)
    except AttributeError as e:
        print("Error accessing __ssn directly: ",e)

    print("SSN (via name mangling):", emp._Employee__ssn)