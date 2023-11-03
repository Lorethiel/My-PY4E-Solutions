text = "X-DSPAM-Confidence:    0.8475"


pos = text.find('0')

rpos = text[pos:]



print(float(rpos))