g= input('Please enter your grade: ')


try:
    grade = float(g)
    
        
except:
    grade = -1.0
if grade == -1.0 or grade > 100 or grade < 0:
    print('Please enter a valid grade')
elif grade > 0.9:
    print('A')
elif grade > 0.8:
    print('B')
elif grade > 0.7:
    print('C')
elif grade > 0.6:
    print('D')
else:
    print('F')
    

