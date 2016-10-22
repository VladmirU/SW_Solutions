def no_boring_zeros(n):
    # your code
    if n == 0:
        return n
    edited_num = n
    while edited_num % 10 == 0:
        edited_num //= 10
        
    return edited_num