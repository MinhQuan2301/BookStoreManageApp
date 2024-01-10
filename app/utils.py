def count_cart(cart):
    total_amount, total_quantity = 0, 0
    print(cart)
    if cart:
        for c in cart.values():
            total_quantity += c['quantity']
            total_amount += c['quantity']*c['Price']

    return {
        "total_amount": total_amount,
        "total_quantity": total_quantity
    }