def decorate(func):
    def wrapper_func(*args):
        return '<html>{}</html>'.format(*args)

    return wrapper_func


@decorate
def myFunct(parametr):
    return (parametr)


print(myFunct('hello'))


# ________________________
def clean_line(line):
    table = ''.maketrans("!.,:;-?", "       ")
    line = line.lower()
    return line.translate(table)


def split_words(cleaned_line):
    words = cleaned_line.split()
    return '\n'.join(words) + '\n'


with open("moby_01.txt") as infile, open("moby_01_clean.txt", "w") as outfile:
    for line in infile:
        cleaned_line = clean_line(line)
        cleaned_words = split_words(cleaned_line)
        outfile.write(cleaned_words)


# ______________________

def getDict(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def getStats(word_dict):
    word_list = list(word_dict.items())
    word_list.sort(key=lambda x: x[1])
    return word_list[:5], word_list[-5:]

words = []
with open("moby_01_clean.txt") as infile:
    for word in infile:
        if word.strip():
            words.append(word.strip())

word_dict = getDict(words)
lasts, most = getStats(word_dict)
print(lasts)
print(most)

