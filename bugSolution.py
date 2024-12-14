def function_with_uncommon_bug(a, b):
    try:
        if a == 0:
            return b
        elif b == 0:
            return a
        else:
            return a / b
    except ZeroDivisionError:
        return "Division by zero"

result = function_with_uncommon_bug(0, 0) 
print(result) # Output: Division by zero