#String program for extracting floating point number from a string

text = "X-DSPAM-Confidence:    0.8475"
number = float(text[(text.find('.')-1):])
print(number)