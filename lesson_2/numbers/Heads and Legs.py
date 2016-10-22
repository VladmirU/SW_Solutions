def animals(heads, legs):
    #return (Chickens, Cows)
    if legs % 2 > 0:
        return "No solutions"
        
    chickens_cows = (2 * heads - legs / 2, legs / 2 - heads)
    
    if chickens_cows[0] >= 0 and chickens_cows[1] >= 0:
        return chickens_cows
    else:
        return "No solutions"