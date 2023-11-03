userinput = input('enter file: ')
if len(userinput) < 1:
    userinput = 'mbox-short.txt'
fhandle = open(userinput)
counts = {}

for lines in fhandle:
    if lines.startswith('From '):
        words= lines.split()
        names = words[1]
        counts[names] = counts.get(names,0) + 1

bigword = None
bigvalue = 0

for key,value in counts.items():
    if value > bigvalue:
        bigvalue = value
        bigword = key

print(bigword,bigvalue)

