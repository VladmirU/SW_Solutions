def is_it_magic_square_zip(source_list):
    len_list = len(source_list)
    count = 0
    transparent_list = zip(*source_list)
    control_sum = sum(source_list[0])
    diagonals = [0, 0]
    while count < len_list:
        if sum(source_list[count]) != control_sum or sum(transparent_list[count]) != control_sum:
            return False
        diagonals[0] += source_list[count][count]
        diagonals[1] += transparent_list[count][count]
        count += 1

    if diagonals[0] != control_sum or diagonals[1] != control_sum:
        return False

    return True


if __name__ == '__main__':
    source_list = input('Input source square matrix to check\n')
    print 'Source matrix is magic - {}'.format(is_it_magic_square_zip(source_list))