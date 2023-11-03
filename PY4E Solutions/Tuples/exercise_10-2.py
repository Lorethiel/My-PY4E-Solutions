fname = input('enter a file name: ')
if len(fname) < 1:
    fname = 'mbox-short.txt'
fhandle = open(fname)
userdict = dict()
userlist = []

for line in fhandle:
    if line.startswith('From '):
        words = line.split()
        time = words[5].split(':')
        hour = time [0]
        userdict[hour] = userdict.get(hour,0) + 1
        


for k,v in userdict.items():
    userlist.append((k,v))

for k,v in sorted(userlist):
    print(k,v)
    


