order_amount = 1200
day = "sat"
membership = "gold"
coupon = True
first_order = False

if order_amount >= 1000:
    if day in ["sat", "sun"]:
        if membership == "gold":
            print("Congratulations!")
            print("You get 30% discount.")
        elif membership == "silver":
            print("You get 20% discount.")
        else:
            print("You get 15% weekend discount.")
    else:
        if coupon:
            print("You get 10% coupon discount.")
        else:
            print("No weekend discount.")
elif order_amount >= 500:
    if first_order:
        print("You get 15% first-order discount.")
    elif coupon:
        print("You get 10% discount.")
    else:
        print("You get 5% discount.")
else:
    if membership == "gold":
        print("You get 5% loyalty discount.")
    else:
        print("No discount.")

print("Thank you for shopping!")