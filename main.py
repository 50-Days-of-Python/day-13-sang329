try:
    item_price = int(input())
    vat = int(input())
    total = item_price + (item_price*(vat/100))
    print(round(total))
except:
    print("Invalid Input")
