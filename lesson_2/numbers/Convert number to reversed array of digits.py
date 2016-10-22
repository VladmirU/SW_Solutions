def digitize(n):

    result = []
    edited_num = n
    while edited_num > 0:
        result.append(edited_num % 10)
        edited_num //= 10
    return result