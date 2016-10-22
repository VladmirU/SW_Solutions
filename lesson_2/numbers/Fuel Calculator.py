def fuelPrice(litres, pricePerLiter):
    #your code here
    discount = 0.05
    total_discount = discount * (litres // 2)

    if total_discount > 0.25:
        total_discount = 0.25
    total_price = litres * (pricePerLiter - total_discount)
    
    return round(total_price, 2)