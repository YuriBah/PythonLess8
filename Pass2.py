def type_log(func):
    def wrap(*args):
        exp = func(*args)
        if len(args) == 1:
            print(f'{args[0]}: {type(el)}')
        else:
            for el in args:
                print(f'{el}: {type(el)}')
        return exp

    return wrap

@type_log
def exp_cub(x, *args):
    return x ** 3

fin = exp_cub(5, 7, 8)
print(fin)