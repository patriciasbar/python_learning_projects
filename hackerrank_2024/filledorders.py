def filledOrders(order, k):
    order_filled = 0
    for item in sorted(order):
        if k >= item and item > 0:    
            order_filled += 1 
            k -= item
    return order_filled


