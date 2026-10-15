# Problem 1: Employee Payroll System with Polymorphism (50 points)
# Description
# Create an employee payroll system using abstract base classes and polymorphism. Different employee types
# calculate pay differently.
# Requirements
# Part A: Abstract Employee Class (15 points)
# Create an abstract Employee class with:
# 1. Constructor that takes name and employee_id
# 2. Abstract method calculate_pay() — each subclass computes pay differently
# 3. Abstract method description() — returns a one-line summary of the employee
# 4. Regular method pay_stub() that returns: "[name] (ID: [employee_id]): $[pay]" (calls
# calculate_pay() internally — this is polymorphism!)
# 5. Static method validate_positive(value, name) that:
# Returns True if value > 0
# Raises ValueError with message "[name] must be positive!" otherwise

# making an abstract class for the employees
from abc import ABC, abstractmethod


# abc is the abstract base class module in Python it makes
class Employee(ABC):
    # making the atributes for what makes an employee
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    # making the pay
    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def description(self):
        pass

    def pay_stub(self):
        pay = self.calculate_pay()
        return f"{self.name} (ID: {self.employee_id}): ${pay}"

    @staticmethod
    def validate_positive(value, name):
        if value > 0:
            return True
        else:
            raise ValueError(f"{name} must be positive!")


# Part B: Concrete Employee Classes (25 points)
# Create three classes that inherit from Employee:
# SalariedEmployee:
# Constructor takes: name, employee_id, annual_salary
# Validate salary is positive using the static method
# calculate_pay() returns annual_salary / 24 (paid twice per month)
# description() returns "Salaried: [name]"
# HourlyEmployee:
# Constructor takes: name, employee_id, hourly_rate, hours_worked
# Validate rate and hours are positive
# calculate_pay() returns hourly_rate * hours_worked for the first 40 hours, plus hourly_rate *
# 1.5 * overtime_hours for any hours beyond 40
# description() returns "Hourly: [name]"
# CommissionEmployee:
# Constructor takes: name, employee_id, base_salary, sales, commission_rate
# Validate all values are positive; commission_rate must also be ≤ 1.0
# calculate_pay() returns base_salary + (sales * commission_rate)
# description() returns "Commission: [name]


# making the employee classes
class SalariedEmployee(Employee):
    def __init__(self, name, employee_id, annual_salary):
        super().__init__(name, employee_id)
        self.annual_salary = annual_salary
        self.validate_positive(annual_salary, "Annual salary")

    def calculate_pay(self):
        return self.annual_salary / 24

    def description(self):
        return f"Salaried: {self.name}"


class HourlyEmployee(Employee):
    def __init__(self, name, employee_id, hourly_rate, hours_worked):
        super().__init__(name, employee_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
        self.validate_positive(hourly_rate, "Hourly Rate")
        self.validate_positive(hours_worked, "Hours Worked")
        
    def calculate_pay(self):
        if self.hoursworked <= 40:
            return self.hourly_rate * self.hours_worked
        else:
            overtime_hours = self.hours_worked - 40
            return (self.hourly_
            
        