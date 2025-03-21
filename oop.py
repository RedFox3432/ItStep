class Car:
    def __init__(self, speed, make,year):
        self.speed = speed
        self.make = make
        self.year = year

    def info(self):
        print("Швидкість авто:", self.speed)
        print("Модель авто:", self.make)
        print("рік:", self.year)

auto = Car(speed=100, make='BMW' , year=2011)
auto.info()

command = input(": ")
if command == "get_info":
    print("Швидкість авто:", auto.speed)
    print("Модель авто:", auto.make)
    print("рік:", auto.year)










class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    def info(self):
        print("Імя працівника:", self.name)
        print("Посада:", self.position)
        print("Зарплата:", self.salary)
    def get_salary_info(self):
        return f"Зарплата працівника {self.name}: {self.salary}"
employee = Employee(name="Тимур", position='продавець', salary=35000)
employee.info()
command = input(": ")
if command == "get_info":
    employee.info()
elif command == "get_salary_info":
    print(employee.get_salary_info())