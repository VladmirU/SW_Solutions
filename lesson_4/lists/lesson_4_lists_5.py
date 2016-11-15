def check_list_items_unique(source_list):
    flat_list = []

    def unpacking_list(source_list):
        for item in source_list:
            if isinstance(item, list):
                unpacking_list(item)
            else:
                flat_list.append(item)

    unpacking_list(source_list)

    return len(flat_list) == len(set(flat_list))


if __name__ == '__main__':
    source_list = input('Please, input list to check\n')
    print 'All items are unique - {}'.format(check_list_items_unique(source_list))