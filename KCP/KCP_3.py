def find_sum_7_math():
    result = []
    for num in range(100, 1000):
        summ = 0
        copy_num = num
        while copy_num > 0:
            summ += copy_num % 10
            copy_num //= 10
        if summ == 7:
            result.append(num)

    return result


def find_sum_7_str():
    result = []
    for num in range(100, 1000):
        str_num = []
        str_num.extend(str(num))
        if sum(map(int, str_num)) == 7:
            result.append(num)

    return result