def super_size(n):
    #your code here
    if n < 12:
        return n
    return int("".join(sorted(map(str,str(n)), reverse = True)))
    
    #Second variant
    #m = []
    #m.extend(str(n))
    #return int("".join(sorted(m, reverse = True)))
    
    #Third variant with only int and math
    #edited_val = n
    #lst = []
    #while edited_val > 0:
	#    lst.append(edited_val % 10)
	#    edited_val //= 10
    #lst = sorted(lst, reverse = True)
    #result = lst[0]
    #for itr in lst[1::]:
	#    result = result * 10 + itr
    #return result