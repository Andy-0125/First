# format specifiers = {value:flags} format a value based on what flags are inserted

# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :0(number) = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma separator
# :% = percentage format

price1 = 3.1415926
price2 = -984447.65
price3 = 324.19920
print(f"price 1 is ${price1:+,.2f}")
print(f"price 2 is ${price2:010}")
print(f"price 3 is ${price3:<10}")
print(f"price 1 is ${price1:>10}")
print(f"price 2 is ${price2:^10}")
print(f"price 3 is ${price3:=+10}")
print(f"price 1 is ${price1: }")
print(f"price 2 is ${price2:,}")
print(f"price 3 is ${price3:%}")
