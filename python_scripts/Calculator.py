"""
Basic Calculator
-----------------
A command-line calculator that supports +, -, *, / on two numbers, repeating until the user chooses to quit.

Concepts covered: functions, if/elif chains, try/except, handling division by zero.
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    else:
        return a / b

def get_number(prompt):
    """Keep asking until the user enters a valid number (int or float)."""
    while True:
        raw = input(prompt)
        try:
            return float(raw)
        except ValueError:
            print("That's not a value number, try again!")

def main():
    print("=== Simple Calculator ===")
    print("Operations: 1) Add  2) Subtract  3) Multiply  4) Divide  5) Quit")
    while True:
        choice = input("\nChoose an operation (1-5): ").strip()
        if choice == "5":
            print("Goodbye!")
            break
        if choice not in {"1", "2", "3", "4"}:
            print("Please enter a number from 1 to 5")
            continue
        
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")

        if choice == "1":
            print(f"Result: {add(num1, num2)}")
        elif choice == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif choice == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif choice == "4":
            result = divide(num1, num2)
            if result is None:
                print("Error: cannot divide by zero.")
            else:
                print(f"Result: {result}")

if __name__ == "__main__":
    main()



