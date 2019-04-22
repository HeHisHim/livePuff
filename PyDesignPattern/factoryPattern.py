"""
工厂模式
工厂模式为类创建提供一种便捷的创建对象的方式, 该方式提供一个入口点来创建类和子类的实例
通常将参数传递给工厂类的特殊方法, 即工厂方法
"""

from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_role(self):
        pass
    
    def __str__(self):
        return "{} - {}, {} years old, {}".format(self.__class__.__name__, self.name, self.age, self.gender)

class Engineer(Employee):
    def get_role(self):
        return "engineering"

class Accountant(Employee):
    def get_role(self):
        return "accountant"

class Admin(Employee):
    def get_role(self):
        return "administrator"

class EmployeeFactory:
    # 根据name参数创建不同的实例
    @classmethod
    def create(cls, name, *agrs):
        name = name.lower().strip()

        if "engineering" == name:
            return Engineer(*agrs)
        elif "accountant" == name:
            return Accountant(*agrs)
        elif "administrator" == name:
            return Admin(*agrs)

engineer = EmployeeFactory.create("Engineering", "John", 23, "M")
accountant = EmployeeFactory.create("Accountant", "Amy", 20, "F")
admin = EmployeeFactory.create("administrator", "Sam", 26, "M")

print(engineer)   # Engineer - John, 23 years old, M
print(accountant) # Accountant - Amy, 20 years old, F
print(admin)      # Admin - Sam, 26 years old, M