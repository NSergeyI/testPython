import mymath
import importlib
# from mymath import pi
print(mymath.pi)
# print(pi)
print(importlib.reload(mymath))

import sys
for line in sys.path:
    print(line)
print('__________________')
print(sys.prefix)

print('__________________')

def f(x):
    print("global    : ", globals())
    print("Entry local: ", locals())
    y = x
    print("Exit  local: ", locals())

print("global_out: ", globals())
z = 2
print("global_out: ", globals())
f(z)
print('________________')

for i in dir(__builtins__):
    print(i)
print('________________')

print(max.__doc__)
print('________________')

import mymodule
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = mymodule.clean_line(line)
        cleaned_words = mymodule.split_words(cleaned_line)
        outfile.write(cleaned_words)

words = []
with open("moby_01_clean.txt") as infile:
    for word in infile:
        if word.strip():
            words.append(word.strip())

word_dict = mymodule.getDict(words)
lasts, most = mymodule.getStats(word_dict)
print(lasts)
print(most)


