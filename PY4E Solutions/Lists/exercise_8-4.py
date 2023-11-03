fname = input('enter a file name: ')
fhandle = open(fname)
numlist = []

for line in fhandle:
    words = line.split()
    for word in words:
        if word not in numlist:
            numlist.append(word)
print(sorted(numlist))