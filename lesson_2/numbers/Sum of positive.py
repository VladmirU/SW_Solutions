def positive_sum(arr):
    # Your code here
    posiv_sum = 0
    for item in arr:
	    if item > 0:
		    posiv_sum += item
    return posiv_sum