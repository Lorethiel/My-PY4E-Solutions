largest = None
smallest = None

while True:
    number = input('enter a number: ' )
    if number == 'done':
        break
    try:
        fnumber = float(number)
    except:
        print('Invalid input')
        continue 
    if largest is None:
        largest = fnumber
    if largest is not None and largest < fnumber:
        largest = fnumber

    if smallest is None:
        smallest = fnumber
    if smallest is not None and smallest > fnumber:
        smallest = fnumber



print('Maximum is',int(largest))
print('Minimum is', int(smallest))