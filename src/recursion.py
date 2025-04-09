# src/recursion.py

def factorial(n):
    """Calculate the factorial of a number using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Example usage
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is {result}.")