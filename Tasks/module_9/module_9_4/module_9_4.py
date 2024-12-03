first = "Мама мыла раму"
second = "Рамена мало было"

print(list(map(lambda x, y: x == y, first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a+') as f:
            for item in data_set:
                if isinstance(item, str):
                    f.write(item + '\n')
                else:
                    f.write(str(item) + '\n')

    return write_everything

writing = get_advanced_writer('module_9_4_file.txt')
writing('Это строка', 5, ["А", "это", "уже", "число", 5, "в", "списке"])

from random import choice

class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return choice(self.words)

first_ball = MysticBall("Да", "Нет", "Наверное")
print(first_ball())
print(first_ball())
print(first_ball())
