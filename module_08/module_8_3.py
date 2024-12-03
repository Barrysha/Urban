class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumber(Exception):
    def __init__(self, message):
        self.message = message

class Car:

    def __init__(self, model, vin, numbers):
        self.model = str(model)

        if not isinstance(vin, int):
            raise IncorrectVinNumber("Некорректный тип vin номера.")
        elif not 1000000 <= vin <= 9999999:
            raise IncorrectVinNumber("Некорректный диапозон vin номера.")
        else:
            self.vin = vin

        if not isinstance(numbers, str):
            raise IncorrectCarNumber("Некорректный тип данных для номера")
        elif len(numbers) != 6:
            raise IncorrectCarNumber("Неверная длина номера")
        else:
            self.numbers = numbers

try:
    first = Car("Model1", 1000000, "f123dj")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    second = Car("Model2", 300, "Михаил")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")

try:
    third = Car("Model3", 2020202, "нет номера")
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumber as exc:
    print(exc.message)
else:
    print(f"{first.model} успешно создан")
