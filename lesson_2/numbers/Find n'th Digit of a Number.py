def find_digit(num, nth):
    #your code here
    if nth <= 0:
        return -1
    else:
        return abs(num) / 10 ** (nth - 1) % 10