def personal_sum(num):
    result = 0
    incorrect_data = 0

    try:
        for i in num:
            try:
                result += i
            except TypeError:
                incorrect_data += 1
    except TypeError:
        return "Некорректный тип данных"

    return (result, incorrect_data)

def calculate_average(num):
    try:
        return personal_sum(num)[0] / (len(num) - personal_sum(num)[1])
    except TypeError:
        return "Некорректный тип данных"
    except ZeroDivisionError:
        return 0

print(personal_sum([0, 1, 2, 3]))
print(personal_sum('Hello, World'))
print(calculate_average(12))
print(calculate_average('Hello, World')) # В ответе 0, потому что нет result == 0
print(calculate_average([0, 1, 2, 3, 4, 5]))
print(calculate_average([0, 1, 'ghb']))
print(calculate_average([])) # В ответе 0, потому что сработало исключение
