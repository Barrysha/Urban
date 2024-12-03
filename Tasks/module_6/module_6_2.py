class Vehicle:

    COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, engine_power, color):
        self.owner = str(owner)
        self.model = str(model)
        self.engine_power = int(engine_power)
        self.color = str(color)

    def get_model(self):
        print(f"Модель: {self.model}")

    def get_horsepower(self):
        print(f"Мощность двигателя: {self.engine_power}")

    def get_color(self):
        print(f"Цвет: {self.color}")

    def print_info(self):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}\n")

    def set_color(self, new_color):
        self.reg_colours = [colour.lower() for colour in self.COLOR_VARIANTS]
        if new_color.lower() in self.reg_colours:
            self.color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}\n")

class Sedan(Vehicle):

    PASSENGERS_LIMIT = 5

vehicle1 = Sedan("Fedos", "Toyota Mark II", 500, "Blue")

vehicle1.print_info()
vehicle1.set_color("PINK")
vehicle1.set_color("BLACK")
vehicle1.owner = "Vasyok"

vehicle1.print_info()
