def calculate_discount(price, discount):
    disc_frac = discount/100
    off_money = price * disc_frac
    new_price = price - off_money
    return new_price

def main(x,y,z,a):
    print(calculate_discount(x,y))
    print(calculate_discount(x,z))
    print(calculate_discount(a,y))
    print(calculate_discount(a,z))

if __name__ == "__main__":
    main(100, 5, 45.5, 99.99)
