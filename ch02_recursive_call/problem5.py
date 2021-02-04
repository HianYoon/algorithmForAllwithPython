def fibonacci(num):
    if num == 1:
        return 0
    elif num == 2:
        return 1

    index = 2

    def calc(first, second):
        nonlocal index
        index = index + 1
        result = first + second
        if index == num:
            return result
        return calc(second, result)

    return calc(0, 1)


print(fibonacci(5))