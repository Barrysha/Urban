from threading import Lock, Thread
from random import randrange
from time import sleep

class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            amount = randrange(50, 401)
            self.balance += amount
            print(f"Пополнение: {amount}. Баланс: {self.balance}")
            if (self.balance >= 500) and self.lock.locked():
                print("Баланс превысил 500, разблокируем замок")
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            amount = randrange(50, 501)
            print(f"Запрос на {amount}")
            if amount <= self.balance:
                self.balance -= amount
                print(f"Снятие: {amount}. Баланс: {self.balance}")
                sleep(0.001)
            else:
                print("Запрос отклонён. Недостаточно средств")
                self.lock.acquire()
                sleep(0.001)


bank = Bank()

th1 = Thread(target=bank.deposit)
th2 = Thread(target=bank.take)

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый быланс: {bank.balance}")
