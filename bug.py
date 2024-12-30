def function_with_uncommon_error(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Type Error"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

#Example usage
print(function_with_uncommon_error(10, 0))  # Output: Division by zero
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, "hello")) # Output: unsupported operand type(s) for /: 'int' and 'str'