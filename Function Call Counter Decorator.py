#Boilerplate Code
from functools import wraps

def count_calls(func):
    # Implement the decorator here
    pass

@count_calls
def example_function():
    print("Function called")

example_function()
example_function()

print(f"example_function has been called {example_function.call_count} times")