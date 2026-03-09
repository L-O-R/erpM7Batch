# phase 1 employees blueprint creation
from abc import ABC, abstractmethod


#1. THE Master Template (Abstract Base Class)
class Entity(ABC):
    @abstractmethod
    def get_details(self):
        """Every child class MUST implement this, or the python will complain"""
        pass


#2. The Employee Blueprint
class Employee(Entity):
    def __init__(self, emp_id: str, name: str, role: str = 'Staff', salary: float = 150000.00):
        # Data is private
        self.__emp_id = emp_id
        self.__name = name
        self.__role = role
        self.__salary = salary
        self.assets = []

    # Getter for Emp id
    @property
    def emp_id(self):
        return self.__emp_id
    # getter and setter for salary
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary: float):
        self.__salary = new_salary


    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def role(self):
        return self.__role

    def get_details(self):
        return f'ID: {self.__emp_id} | Name: {self.__name} | Role: {self.__role} | Salary: {self.__salary}'

    # Dunder method: Making our object behave like real data
    def __str__(self):
        return self.get_details()
    def __repr__(self):
        return self.get_details()
    def __eq__(self, other):
        return self.__emp_id == other.emp_id


#3. THe manager Class(Inherits From Employee)
class Manager(Employee):
    def __init__(self, emp_id: str, name: str, role: str = 'Manager', salary: float = 150000.00, bonus:float=1000):
        super().__init__(emp_id, name, role, salary)
        self.__bonus = bonus
    #  polymorphism=> method overriding will change the parent class method in child class
    @property
    def bonus(self):
        return self.__bonus
    @bonus.setter
    def bonus(self, new_bonus: float):
        self.__bonus = new_bonus


    def get_details(self):
        base = super().get_details()
        return f'{base} | Bonus: {self.__bonus}'


manager1 = Manager('E01', 'Bob', "Manager", 14000.00, 2000.00)

print(manager1)