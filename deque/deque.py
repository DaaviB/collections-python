from collections import deque

cache_values = deque(maxlen=3)


def cache(func):
    def inner(*args):
        cache_values.append((args, args[0]+args[1]))
        return func(*args)
    return inner



@cache
def soma(x, y):
    return x + y

if __name__ == '__main__':
    soma(2, 4)
    print(cache_values)
