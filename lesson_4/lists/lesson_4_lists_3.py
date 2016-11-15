import random

def gen_list():
    test_list = []
    ran_range = range(-5, 20)
    columns = random.randint(2, 5)
    return [random.sample(ran_range, columns) for row in range(random.randint(2, 5))]


def set_sum_to_last_row_item(source_list):
    result_list = []
    for row in source_list:
        row[-1] = sum(row[:-1])
        result_list.append(row)
    return result_list

if __name__ == "__main__":
    test = gen_list()

    print 'Original list is\n', test
    print 'Modified list is\n', set_sum_to_last_row_item(test)