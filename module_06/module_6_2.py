class Vehicle:

    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f"Владелец: {self.owner}\n")

    def set_color(self, new_color):
        self.reg_colours = [colour.lower() for colour in self.__COLOR_VARIANTS]
        if new_color.lower() in self.reg_colours:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}\n")

class Sedan(Vehicle):

    __PASSENGERS_LIMIT = 5

vehicle1 = Sedan("Fedos", "Toyota Mark II", 500, "Blue")

vehicle1.print_info()
vehicle1.set_color("PINK")
vehicle1.set_color("BLACK")
vehicle1.owner = "Vasyok"

vehicle1.print_info()
