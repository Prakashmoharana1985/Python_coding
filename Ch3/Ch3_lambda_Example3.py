# Ch3 Lambda_Example3.py


def timesTables(n):
    return tuple(filter(lambda x: not x % 7, range(1, n)))


print(timesTables(77))
