def custom_fibonacci(nth):
    if nth == 1 or nth == 2:
        return 1
    prev_cur = [1 , 1]
    for iterator in range(2,nth):
        current = sum(prev_cur)
        prev_cur[0], prev_cur[1] = prev_cur[1], current

    return current

print "Input what Fibonacci num want to find"
nth = input()
print "The {0} fibonacci number is {1}".format(nth,custom_fibonacci(nth))