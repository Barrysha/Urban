def add_everything_up(a, b):
     try:
        return a + b
     except TypeError:
         return str(a) + str(b)

print(add_everything_up(17, 'ghbd'))
print(add_everything_up(17, 42))
