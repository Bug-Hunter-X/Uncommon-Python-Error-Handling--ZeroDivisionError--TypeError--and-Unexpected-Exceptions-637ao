def function_with_uncommon_error(a, b):
    try:
        if isinstance(b, (int, float)) and b != 0:
            result = a / b
            return result
        elif not isinstance(b,(int, float)):
            raise TypeError("Unsupported operand type(s) for /: must be int or float")
        else:
            raise ZeroDivisionError("Division by zero")
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return f"Type Error: {e}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example usage
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, "hello")) # Output: Type Error: Unsupported operand type(s) for /: must be int or float