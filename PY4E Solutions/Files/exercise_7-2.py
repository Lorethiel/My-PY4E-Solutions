fname = input('enter a file name: ')
fhandle = open(fname,'r')
numcount = 0
s=0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        spos = line.find(' ')
        vpos = float(line[spos:])
        numcount = numcount + 1
        s = s + vpos



avgspm = s/numcount  

print('Average spam confidence:',avgspm)