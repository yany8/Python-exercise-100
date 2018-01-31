import string
a =input("please enter a sentence\n")
letter = 0
space = 0
digit = 0
others = 0
for i in a:
    if i.isalpha():
        letter += 1
    elif i.isspace():
        space += 1
    elif i.isdigit():
        digit += 1
    else:
        others += 1
print("letters: %d, space: %d, digit: %d, others: %d" % (letter,space,digit,others))
