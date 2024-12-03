animal = "мишка"
animals = ["зайка","мишка","бегемотик"]

def gen_repeat(n):

    def repeat(animal):
        return (animal[:2] +'-') * n + animal

    return repeat

test1 = gen_repeat(1)
test2 = gen_repeat(2)

print(test1(animal))
print(test2(animal))

repetition = [gen_repeat(n) for n in range(1, 4)]
print(repetition)

result = [func(animal) for func in repetition   ]
print(result)

fin_result = [func(x) for func in repetition for x in animals]
print(fin_result)

def memoize_func(f):
    mem = {}

    def wrapper(*args):
        print(f"Выполняем  функцию с аргументами={args}, внутренняя память={mem}")
        if args not in mem:
            mem[args] = f(*args)
            return f"Функция выполнилась, ответ {mem[args]}"
        else:
            return f"Функция уже была выполнена раньше, ответ {mem[args]}"
    return wrapper

@memoize_func
def func(a, b):
    print(f"Выполняем функцию с аргументами {a}, {b}")
    return a ** b

print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 2), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')


