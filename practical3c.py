global_message = "Hello, I am F115 Dhani"
global_number = 15

class MyClass:
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print(f"Instance name: {self.name}")
        print(f"Global message accessed from within the class: {global_message}")

    def perform_calculation(self, adder):
        result = global_number + adder
        print(f"Calculation: {global_number} + {adder} = {result}")
        return result

print(f"Initial global number: {global_number}")
global_number += 50
print(f"Modified global number: {global_number}")

my_object = MyClass("Dhani")

my_object.display_info()
calculated_value = my_object.perform_calculation(3)
print(f"Value returned from calculation: {calculated_value}")

print(f"Global number after class interactions: {global_number}")
