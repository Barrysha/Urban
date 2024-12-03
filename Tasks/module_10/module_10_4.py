from threading import Thread
from random import randint
from time import sleep
from queue import Queue

class Table():

    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):

    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def run(self):
        sleep(randint(3, 11))


class Cafe():
    def __init__(self, *tables: Table):
        self.queue = Queue()
        self.tables = tables

    def is_vacant(self):
        return not any(t.guest for t in self.tables)

    def guest_arrival(self, *guests: Guest):
        for guest in guests:
            vacant_table_found = False
            for table in self.tables:
                if not table.guest:
                    table.guest = guest
                    guest.start()
                    print(f"{guest.name} сел(-а) за стол номер {table.number}.")
                    vacant_table_found = True
                    break
            if not vacant_table_found:
                self.queue.put(guest)
                print(f"{guest.name} в очереди.")

    def discuss_guests(self):
        while not (self.queue.empty() and self.is_vacant()):
            for table in self.tables:
                if not table.guest:
                    if not self.queue.empty():
                        table.guest = self.queue.get()
                        print(f"{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}.")
                        table.guest.start()
                else:
                    if not table.guest.is_alive():
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла).")
                        table.guest = None
                        print(f"Стол номер {table.number} свободен.")



if __name__ == "__main__":
    tables = [Table(number) for number in range(1, 6)]

    guests_names = [
        "Maria", "Oleg", "Vakhtang", "Sergey", "Darya", "Arman",
        "Viktoria", "Nikita", "Galina", "Pavel", "Ilya", "Alex"
        ]

    guests = [Guest(name) for name in guests_names]

    cafe = Cafe(*tables)

    cafe.guest_arrival(*guests)

    cafe.discuss_guests()
