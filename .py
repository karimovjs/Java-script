def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def main():
    """Runs the main calculator input loop."""
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("Enter 'q' to exit.")

    while True:
        # Get user choice for the operation
        choice = input("\nEnter choice (1/2/3/4 or q): ").strip()

        # Check if user wants to quit
        if choice.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        # Validate operation choice
        if choice not in ('1', '2', '3', '4'):
            print("Invalid input. Please enter 1, 2, 3, 4, or q.")
            continue

        try:
            # Get numbers from user, handle non-numeric input
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform calculation based on choice
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                # Attempt division, which might raise ValueError
                print(f"{num1} / {num2} = {divide(num1, num2)}")

        except ValueError as e:
            # catch input conversion errors or division by zero
            print(f"Error: {e}")
        except Exception as e:
            # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()