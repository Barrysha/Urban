import time
from threading import Thread

class Knight(Thread):

    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemies = 100
        self.battle_days = 0

    def run(self):
        print(f"{self.name}, на нас напали!")
        while self.enemies > 0:
            if self.power > self.enemies:
                self.enemies = 0
            else:
                self.enemies -= self.power
            self.battle_days += 1
            print(f"{self.name} сражается {self.battle_days}..., осталось {self.enemies} воинов.")
            time.sleep(1)
        print(f"{self.name} одержал победу спустя {self.battle_days} дней!\n")


knight1 = Knight("Sir William", 20)
knight2 = Knight("Lady Anne", 10)
knight3 = Knight("Superman", 101)

knight1.start()
knight2.start()
knight3.start()

knight1.join()
knight2.join()
knight3.join()

print("Битва окончена!")
