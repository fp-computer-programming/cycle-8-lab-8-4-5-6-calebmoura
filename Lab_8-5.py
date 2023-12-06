# Author: Caleb Moura

# Function to calculate factorial of a number with parameters and returns on the input number.
def factorial(num):
    
    # Base case: factorial of 0 or 1 is 1.
    if num == 0 or num == 1:
        return 1
    else:
        # Recursive case: num * factorial of (num-1)
        return num * factorial(num - 1)

# Example usage of factorial function.
if __name__ == "__main__":
    # Prompt user for input.
    num_input = int(input("Enter a number to calculate its factorial: "))

    # Call factorial function and display result.
    result = factorial(num_input)
    print(f"The factorial of {num_input} is: {result}")