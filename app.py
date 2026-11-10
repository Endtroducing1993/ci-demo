def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    result1 = add(4, 5)
    result2 = sub(10, 3)
    result3 = multiply(4, 5)
    result4 = divide(10, 3)

    print(result1, result2)
