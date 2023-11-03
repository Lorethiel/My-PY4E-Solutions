fname = input('enter a file name: ')
fhandle = open(fname)
count = 0

for line in fhandle:
    if len(line) > 2 and line.startswith('From '):
        mails = line.split()
        print(mails[1])
        count = count + 1
print('There were', count, "lines in the file with From as the first word")
