def add_items_to_zero_sum(incoming_list):
    summ = sum(incoming_list)
    if abs(summ) < 10:
        incoming_list.append(-summ)
        return incoming_list
    while abs(summ) > 8:
        if abs(summ) - 9 >= 0:
            if summ > 0:
                incoming_list.append(-9)
            else:
                incoming_list.append(9)
        summ -= 9
    if abs(summ) > 0:
        if summ > 0:
            incoming_list.append(-summ)
        else:
            incoming_list.append(summ)
    return incoming_list