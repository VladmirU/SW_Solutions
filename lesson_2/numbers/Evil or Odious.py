# solution with string
#def evil(n):
#    count = 0
#    for one_bit in "{0:b}".format(n):
#        if one_bit == '1':
#            count += 1
#    if count & 1 == 0:
#        return "It's Evil!"
#    else:
#        return "It's Odious!"

# Solution with math
def evil(n):
    edited_number = n
    count = 0
    while edited_number > 0:
    	if edited_number % 2 == 1:
    		count += 1
    	edited_number //= 2
    if count & 1 == 0:
        return "It's Evil!"
    else:
        return "It's Odious!"