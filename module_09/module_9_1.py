def apply_all_func(int_list, *functions):
    result = {}

    for f in functions:
        fname = f.__name__
        try:
            resultat = f(int_list)
            result[fname] = resultat
        except TypeError:
            pass
    return [i for i in result.items()]

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*apply_all_func(int_list, len, sum, min, sorted), sep='\n', end='\n')
