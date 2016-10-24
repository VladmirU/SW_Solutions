def factorial(num):
    if num == 0:
        return 1
    current = 1
    for iterator in range(1,num+1):
        current *= iterator

    return current

print "Input num to count Factorial"
num = input()
print "Factorial of the", num, "is",factorial(num)