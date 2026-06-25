# When a customer places an order, we need to:

#         1. Calculate Total Cart Amount
#         2. Apply Discount
#         3. Add Delivery Charges
#         4. Generate Final Bill

# If cart_amount >= 5000 then apply 2% discount

# If cart_amount >= 3000 then apply 1% discount

# if cart_amount >=1000 then delivery charge is 0 else delivery charge is 50 INR

def calculate_discount(cart_amount):
    if cart_amount>=5000:
        return cart_amount*0.02
    elif cart_amount>=3000:
        return cart_amount*0.01
    return 0

def delivery_charge(cart_amount):
    if cart_amount>= 1000:
        return 0
    return 50
def generate_bill (cart_amount):
    discount= calculate_discount(cart_amount)
    delivery= delivery_charge(cart_amount)
    
    final_bill= cart_amount- discount + delivery
    
    print("Cart amount : ", cart_amount)
    print("Discount : ", discount)
    print("Delivery Charge : ", delivery)
    print("Final Bill  : ", final_bill)
    
    
cart_amount= eval(input("Enter the value"))
generate_bill(cart_amount)