x = [1, 3, 5, 0, -1, 3, -2]
for i, n in enumerate(x):
    if n < 0:
        del x[i]
print(x)

x = [1, 3, 5, 0, -1, 3, -2]
for n in x:
    if n < 0:
        x.remove(n)
print(x)

y = [[1, -1, 0], [2, 5, -9], [-2, -3, 0]]
count = 0
for n in y:
    for nn in n:
        if nn < 0:
            count += 1
print(count)

x = 8
str = ''
if x < -5:
    str = 'very low'
elif x < 0:

    str = 'low'
elif x == 0:
    str = 'neutral'
elif x <= 5:
    str = 'high'
elif x > 5:
    str = 'very hifh'
print(str)

x = [1, 3, 5, 0, -1, 3, -2]
without_minus = [item for item in x if item > 0]
print(without_minus)

one_100 = range(101)
even = (item for item in one_100 if item % 2 == 0 and item > 0)
for i in even:
    print(i)

eleven_15 = range(11, 16)
kub = {item: item ** 3 for item in eleven_15}
print(kub)

""" Читает файл и возвращает количество строк, слов
и символов - по аналогии с утилитой UNIX wc
"""
table = ''.maketrans("!.,:;-?", "       ")
line_count = 0
word_count = 0
char_count = 0

with open('word_count.tst') as infile:
    for line in infile:
        line_count += 1
        char_count += len(line)
        line = line.translate(table)
        word_count += len(line.split())
print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))
