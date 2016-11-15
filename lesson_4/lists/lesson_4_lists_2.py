import random


def gen_list():
    test_list = []
    ran_range = range(-5, 20)
    columns = random.randint(2, 5)
    for row in range(random.randint(2, 5)):
        test_list.append(random.sample(ran_range, columns))

    return test_list


def check_unique_set(source_list):
    compare_list = []
    for row in source_list:
        compare_list.extend(row)
    return len(compare_list) == len(set(compare_list))


def check_unique(source_list): #Solution without set()
    compare_list = []
    for row in source_list:
        for item in row:
            if item in compare_list:
                return False
            else:
                compare_list.append(item)
    return True


if __name__ == '__main__':
    test_list = gen_list()
    print 'Source list is'
    for row in test_list:
        print row
    print 'Items in list unique - {}'.format(check_unique_set(test_list))