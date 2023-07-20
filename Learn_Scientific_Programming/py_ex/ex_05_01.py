number = 0
total = 0

while True:
    number = input('input a number ')
    if number == 'done' or number == 'Done':
        break
    try:
        number_in_float = float(number)
    except:
        print('invalid')
        # if you use countinue, looping gonna back to top without end the loop
        continue
    total = total + number_in_float

print('the total is', total)
