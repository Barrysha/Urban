def is_prime(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        # Проверяем на множетели
        if str(res)[-1]==5 or (res%2==0 and res!=0) or (sum([int(i) for i in str(res)])%3==0 and res!=0):
            print("Сложное")
        else:
            print("Простое")
        return res
    return wrapper

@is_prime
def sum_three(*args):
    return sum(args)

a = sum_three(2, -20, 5, 6, 7)

print(a)
