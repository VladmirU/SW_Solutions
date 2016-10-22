def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    total_sum = 0
    for mult in range(n, m):
        if mult % n == 0:
            total_sum += mult
            
    return total_sum
    
# With while loop
'''
def sum_mul(n, m):
    if m <= 0 or n <= 0:
        return 'INVALID'
    total_sum = 0
    count = n
    while count < m:
        if count % n == 0:
            total_sum += count
        count += 1
            
    return total_sum
'''