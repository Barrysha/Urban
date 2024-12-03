class Figure: # Начало написания 17.10 22:40. Припозднился, да.

    sides_count = 0 # Количество сторон

    def __init__(self, color=[0, 0, 0], sides=None):
        self.sides = sides if sides is not None else []
        self.color = color
        self.filled = False
        Figure.sides_count = len(self.sides)

    def get_color(self): # Возвращаем rgb список
        return self.color

    def set_color(self, rgb):
        # Метод is_valid_color вписал в условие этого метода за ненадобностью.
        # Заодно заменил 3 параметра (r, g, b) на один список. Если нужно оформить инпут, можно сделать генератор, выключающийся после 3х вводов. так что пойдёт.
        if isinstance(rgb, list) and all(0 <= val <= 255 for val in rgb):
            self.color = rgb
        else:
            print("Цвет не попадает в диапозон rgb")

    def get_sides(self): # Выводим стороны
        return self.sides

    def set_sides(self, new_sides):
        # Меняем стороны, если новые стороны удовлетворяют условиям
        if not self.is_valid_sides(new_sides):
            print("Недопустимое количество сторон")
            return
        self.sides = new_sides

    def is_valid_sides(self, sides): # Условия для смены сторон
        if not isinstance(sides, list):
            return False
        if len(sides) != self.sides_count:
            return False
        return all(isinstance(side, int) and side > 0 for side in sides)

    def __len__(self): # Периметр
        return sum(self.sides)

class Circle(Figure):

    sides_count = 1

    def __init__(self, color=[0, 0, 0], sides=None):
         super().__init__(color, sides)
         if len(self.sides) != self.sides_count:
            self.sides = [1]

    def radius(self):
        return (sum(self.sides) / (2 * 3.14))

    def get_S(self): # Площадь
        return (sum(self.sides) / 2) ** 2

class Triangle(Figure):

    sides_count = 3

    def __init__(self, color=[0, 0, 0], sides=None):
        super().__init__(color, sides)
        if len(self.sides) != self.sides_count:
            self.sides = [1, 1, 1]

    def get_S(self): # Находим площадь через формулу Герона
        p = sum(self.sides) / 2
        return ((p*(p-self.sides[0])*(p-self.sides[1])*(p-self.sides[2]))**0.5)

class Cube(Figure):

    sides_count = 12

    def __init__(self, color=[0, 0, 0], sides=None):
        super().__init__(color)
        self.sides = [sides for i in range(self.sides_count)]

    def get_volume(self):
        return self.sides[0]**3

    def get_S(self): # Добавил от себя площадь сторон куба
        return (self.sides[0]**2)*6


circle1 = Circle([200, 200, 100], [10])
cube1 = Cube([222, 35, 130], 6) # Очень хочу эту шестёрку тоже в список закинуть, но всё ломается, и мозги уже отказываются решать это.

# Проверка на изменение цвета
circle1.set_color([55, 66, 77])
print(circle1.get_color()) # YES
cube1.set_color([1, -2, 3])
print(cube1.get_color(), '\n') # NO

# Проверка на изменение сторон
cube1.set_sides([12, 14, 15])
print(cube1.get_sides()) # NO
circle1.set_sides([15])
print(circle1.get_sides(), '\n') # YES

# Проверка периметра круга
print(len(circle1), '\n')

# Проверка объёма куба
print(cube1.get_volume())

# 18.10 02:53
