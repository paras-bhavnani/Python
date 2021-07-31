import timeit
def function_timer(function):
    def wrapper():
        print(timeit.timeit(stmt =function, number = 1))
        return timeit.timeit(stmt =function, number = 1)
    return wrapper

@function_timer
def sayHi():
    print('Hi everyone!')

sayHi()