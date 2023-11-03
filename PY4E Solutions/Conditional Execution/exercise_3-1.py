h = input('Please enter how many hours you work ')
r = input('Please enter rate ')

rate = float(r)
hours = float(h)


if hours <= 40:
    print(hours*rate)
else:
    print(40*rate + (hours - 40)*(rate*1.5))