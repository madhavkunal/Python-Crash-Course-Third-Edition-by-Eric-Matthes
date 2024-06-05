import pytest
from employee import Employee

@pytest.fixture # decorator fixture
def employee(): # create employee generator/decorator function
    Bob = Employee("Bob", "Evans", 130000)  # create Bob as an Employee
    return Bob

def test_give_default_raise(employee):
    employee.give_default_raise()    # use class method on Bob giving Bob standard annual $5000 raise
    # test if class method works by checking if annual_salary value is correctly updated
    assert employee.annual_salary == 135000
    # remember == checks if two values are equal
    # remember = checks if two objects are the same instance in memory


def test_give_custom_raise(employee):
    employee.give_custom_raise(20000)  # use class method on Bob giving Bob a $20,000 raise
    # test if class method works by checking if annual_salary value is correctly updated
    assert employee.annual_salary == 150000
    # remember == checks if two values are equal
    # remember = checks if two objects are the same instance in memory


"""

def test_give_default_raise():
    Bob = Employee('Bob', 'Evans', 130000)  # create Bob as an Employee
    Employee.give_default_raise(Bob)    # use class method on Bob giving Bob standard annual $5000 raise
    # test if class method works by checking if annual_salary value is correctly updated
    assert Bob.annual_salary == 135000
    # remember == checks if two values are equal
    # remember = checks if two objects are the same instance in memory


def test_give_custom_raise():
    Bob = Employee("Bob", "Evans", 130000)  # create Bob as an Employee
    Employee.give_custom_raise(Bob, 20000)  # use class method on Bob giving Bob a $20,000 raise
    # test if class method works by checking if annual_salary value is correctly updated
    assert Bob.annual_salary == 150000
    # remember == checks if two values are equal
    # remember = checks if two objects are the same instance in memory

"""
