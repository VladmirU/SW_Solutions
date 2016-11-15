import random


def gen_list():
    test_list = []
    ran_range = range(-100, 100)
    columns = random.randint(2, 5)
    for row in range(random.randint(2, 5)):
        test_list.append(random.sample(ran_range, columns))

    return test_list


def average_neg(source_list):
    count = 0
    summ = 0
    for row in source_list:
        for item in row:
            if item < 0:
                summ += item
                count += 1
    return float(summ) / count

if __name__ == '__main__':
    test_list = gen_list()
    print 'Source list is'
    for row in test_list:
        print row
    print 'Average value of negative numbers is {}'.format(average_neg(test_list))