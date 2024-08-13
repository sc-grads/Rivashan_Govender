def divide(dividend, divisor):
    if divisor == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return dividend / divisor

def calculate(*args, operator):
    return operator(*args)

result = calculate(20, 4, operator=divide)
print(result)  # Output: 5.0

def search(sequence, expected, finder):
    for item in sequence:
        if finder(item) == expected:
            return item
    raise RuntimeError(f"Could not find an element with expected value: {expected}")


def get_friend_name(friend):
    return friend['name']

friends = [
    {'name': 'Rolf Smith', 'age': 24},
    {'name': 'Alice Johnson', 'age': 30},
    {'name': 'Bob Smith', 'age': 28}
]

result = search(friends, 'Bob Smith', get_friend_name)
print(result)  # Output: {'name': 'Bob Smith', 'age': 28}


result = search(friends, 'Bob Smith', lambda friend: friend['name'])
print(result)  # Output: {'name': 'Bob Smith', 'age': 28}

from operator import itemgetter

result = search(friends, 'Bob Smith', itemgetter('name'))
print(result)  # Output: {'name': 'Bob Smith', 'age': 28}




