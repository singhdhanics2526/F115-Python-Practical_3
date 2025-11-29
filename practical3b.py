class MyClass:
    def method_one(self, first_value):
        print(f"Inside method_one: First value received: {first_value}")
        returned_value = self.method_two(first_value)
        final_result = returned_value * 3
        print(f"Inside method_one: Value returned from method_two: {returned_value}")
        print(f"Inside method_one: Final result after processing: {final_result}")
        return final_result

    def method_two(self, input_value):
        processed_value = input_value + 30
        print(f"Inside method_two: Processing input value: {input_value}")
        return processed_value

my_object = MyClass()

result_from_object = my_object.method_one(10)

print(f"\nProgram execution complete. Result returned to main scope: {result_from_object}")
