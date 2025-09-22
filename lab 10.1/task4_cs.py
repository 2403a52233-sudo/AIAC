def welcome(name):
    """Reusable function to generate welcome message."""
    return f"Welcome {name}"

def greet_all(names, greeting_func):
    """Reusable function to greet all people using any greeting function."""
    for name in names:
        print(greeting_func(name))

# Demonstrate modularity
students = ["Alice", "Bob", "Charlie"]
greet_all(students, welcome)
