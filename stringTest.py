import string

print('x')
print('\155')
print('\x6D')

unicode_a_with_acute = '\N{LATIN SMALL LETTER A WITH ACUTE}'
print(unicode_a_with_acute)
unicode_a_with_acute = '\u00E1'
print(unicode_a_with_acute)
unicode_a = '\N{LATIN SMALL LETTER A}'

print(unicode_a)
print('a\n\tb')
'a\n\tb'
print('abc\n')
print('abc\n', end='')
print('end')

test_join = ' '.join(["join", "puts", "spaces", "between", "elements"])
print(test_join)
test_join2 = "::".join(["Separated", "with", "colons"])
print(test_join2)
test_join3 = "".join(["Separated", "by", "nothing"])
print(test_join3)
print('----------------------------')
test_join4 = '\n'.join([test_join, test_join2, test_join3])
print(test_join4)

x = "You\t\t can have tabs\t\n \t and newlines \n\n " \
    "mixed in"
print(x.split())
x = "Mississippi"
print(x.split('ss'))
x = 'a b c d'
print(x.split(' ', 1))
print(x.split(' ', 2))
print(x.split(' ', 9))
print('--------------')
print(x.split(None, 9))

x = "this is a test"
x = x.split()
x = '-'.join(x)
print(x)

# import string
# print(string.whitespace)

x = "Mississippi"
print(x.find("ss", 3))
print(x.find("ss", 0, 3))
print(x.count("ss"))
print(x.startswith('Miss'))
print(x.endswith('Miss'))
print(x.endswith('ppi'))
print(x.endswith(("i", "u")))

test = 'Допустим, вы хотите проверить, завершается ли строка подстрокой rejected'
print(test.endswith('rejected'))
if test.rfind('rejected') == (len(test) - len('rejected')):
    print('Yes')
else:
    print('No')
print(test[-8:] == 'rejected')
print(x.replace("ss", "+++"))

x = "~x ^ (y % z)"
table = x.maketrans("~^()", "!&[]")
print(x.translate(table))

x = "!#@@$##%$^%^*&*()()(*_)(_)KJHGGHFGD46554^%^%&^%&*&*"
table = x.maketrans("~!@#$%^&*()_+,.", "               ")
print(x.translate(table))

print('------------')
x = "123"
print(x.isdigit())
print(x.isalpha())
x = "M"
print(x.islower())
print(x.isupper())

print(string.whitespace)
print(string.digits)
print(string.hexdigits)

x = ['"abc"', 'def', '"ghi"', '"klm"', 'nop']
y = []
for word in x:
    y.append(word.replace('"', ''))
print(y)

x = "Mississippi"
pos = x.rfind('p')
x = list(x)
x[pos:pos + 1] = []
x = ''.join(x)
print(x)

print(repr(string))
print(str(string))
print(repr(x))
print(str(x))

x = "{0} is the {1} of {2}".format("Ambrosia", "food", "the gods")
print(x)
x = "{{Ambrosia}} is the {0} of {1}".format("food", "the gods")
print(x)
x = "{{{0}}} is the {1} of {2}".format("Ambrosia", "food", "the gods")
print(x)

x = "{1:{0}}".format(3, 4)
print(x)
x = "{0:$>5}".format(3)
print(x)
x = "{a:{b}}".format(a=1, b=5)
print(x)
x = "{a:{b}}:{0:$>5}".format(3, 4, a=1, b=5, c=10)
print(x)

x = "%s is the %s of %s" % ("Ambrosia", "food", "the gods")
print(x)

x = [1, 2, "three"]
x = "The %s contains: %s" % ("list", x)
print(x)

x = "Pi is <%-6.2f>" % 3.14159  # Форматная последовательность %–6.2f
x = "Pi is <%-5.2f>" % 3.14159  # Форматная последовательность %–6.2f
print(x)

num_dict = {'e': 2.718, 'pi': 3.14159}
print("%(pi).2f - %(pi).4f - %(e).2f" % num_dict)

print("a", "b", "c")
print("a", "b", "c", sep="|")
print("a", "b", "c", end="\n\n")

print("a", "b", "c", sep="|", file=open("testfile.txt", "w"))

x = "%(a).08f" % {'a': 1.1111}
print(x)

table = ''.maketrans("!.,:;-?", "       ")
cleaned_words = ''
with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        line = line.lower()
        line = line.translate(table)
        line = line.split()
        # line = '\n'.join(line)
        line = '\n'.join(line) + '\n'
        outfile.write(line)
        # cleaned_words = cleaned_words + line
# Привести к одному регистру
# Удалить знаки препинания
# Разбить на слова
# Записать все слова по одному на строку файла
# outfile.write(cleaned_words)
# cleaned_words
