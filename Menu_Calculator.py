
while True:
    print('To use this program, type the number of the menu item you would like to order.\n\n')
    print('1. Chicken Strips - $3.50.')
    print('2. French Fries - $2.50.')
    print('3. Hamburger - $4.00.')
    print('4. Hotdog - $3.50.')
    print('5. Large Drink - $1.75.')
    print('6. Medium Drink - $1.50.')
    print('7. Milk Shake - $2.25.')
    print('8. Salad - $3.75.')
    print('9. Small drink - $1.25.\n\n')

    order_input = input('Type the number(s) of your order item(s) here: ')
    order = [digit for digit in order_input]

    order_prices = {'1': 3.50, '2': 2.50, '3': 4.00, '4': 3.50, '5': 1.75, '6': 1.50, '7': 2.25, '8': 3.75, '9': 1.25}
    total_cost = 0


    for item in order:
        total_cost = total_cost + order_prices[item]

    print('Your order total is: ${}.\n'.format(total_cost))
    restart = input('To restart this program, press enter.')
