import time


def timer(func):
    def tmp_func(*args, **kwargs):
        start_time = time.time()
        calc_fact = func(*args, **kwargs)
        print "%f" % (time.time()-start_time)
        return calc_fact
    return tmp_func

@timer
def loop_factorial(num):
    if num == 0:
        return 1
    current = 1
    for iterator in range(1, num+1):
        current *= iterator
    return current

@timer
def reduce_factorial(num):
    return 1 if num == 0 else reduce(lambda item1, item2: item1 * item2, range(1, num + 1))

@timer
def recursion_factorial(num):
    def recursion(num):
        if num == 0:
            return 1
        return num * recursion(num - 1)
    recursion(num)


loop_factorial(9999)

reduce_factorial(9999)

recursion_factorial(990)