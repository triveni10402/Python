"""def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)  
    return average

numbers = [10, 20, 30]
result = calculate_average(numbers)
print("Average:", result)"""



"""try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print("Result:", result)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except ValueError:
    print("Invalid input. Please enter a valid number.")"""



"""class ErrorCodes:
    SUCCESS = 0
    EMPTY_LIST = 1
    INVALID_INPUT = 2


def calculate_average(numbers):
    if not isinstance(numbers, list):  # Check for invalid input type
        return None, ErrorCodes.INVALID_INPUT
    if not numbers:  # Check for an empty list
        return None, ErrorCodes.EMPTY_LIST

    try:
        total = sum(numbers)
        average = total / len(numbers)
        return average, ErrorCodes.SUCCESS
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None, ErrorCodes.INVALID_INPUT

test_cases = {
    "valid_case": [10, 20, 30],
    "empty_case": [],
    "invalid_case": "not a list"
}

for case, numbers in test_cases.items():
    result, error_code = calculate_average(numbers)
    if error_code == ErrorCodes.SUCCESS:
        print(f"{case}: Average = {result}")
    elif error_code == ErrorCodes.EMPTY_LIST:
        print(f"{case}: Error - The list is empty.")
    elif error_code == ErrorCodes.INVALID_INPUT:
        print(f"{case}: Error - Invalid input provided.")"""


class ErrorCodes:
    SUCCESS = 0
    EMPTY_LIST = 1
    INVALID_INPUT = 2

def calculate_average(numbers):
    if not isinstance(numbers, list):  
        return None, ErrorCodes.INVALID_INPUT
    if numbers == None:  
        return None, ErrorCodes.EMPTY_LIST

    total = sum(numbers)
    average = total / (len(numbers) - 1)  
    return average, ErrorCodes.SUCCESS

test_cases = {
    "valid_case": [10, 20, 30],
    "empty_case": [],
    "invalid_case": "not a list"
}

for case, numbers in test_cases.items():
    result, error_code = calculate_average(numbers)
    if error_code == ErrorCodes.SUCCESS:
        print(f"{case}: Average = {result}")
    elif error_code == ErrorCodes.EMPTY_LIST:
        print(f"{case}: Error - The list is empty.")
    elif error_code == ErrorCodes.INVALID_INPUT:
        print(f"{case}: Error - Invalid input provided.")













































