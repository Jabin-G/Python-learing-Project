order_amount= 1000
days ="mon"
membership ='NA'

if(order_amount >= 1000 and days in ['sat','sun'] or membership >= 'gold'):
    print("discount 20%")
else:
    print("no discount")