try:
    h = float(input('enter hours: '))
    r = float(input('enter rate: '))
except:
    print('please enter a valid number')




def computepay(h,r):
  
    if h <= 40:
        pay = h * r
    elif h >= 40:
        pay = (40 * r) + (h - 40) * (r * 1.5)
    else:
        print('please enter a valid number')
        
    return pay
    

x = computepay(h,r)

print('Pay',x)
