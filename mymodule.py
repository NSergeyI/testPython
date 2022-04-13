def clean_line(line):
    table = ''.maketrans("!.,:;-?", "       ")
    line = line.lower()
    return line.translate(table)


def split_words(cleaned_line):
    words = cleaned_line.split()
    return '\n'.join(words) + '\n'

def getDict(words):
    result = {}
    for word in words:
        result[word] = result.get(word, 0) + 1
    return result

def getStats(word_dict):
    word_list = list(word_dict.items())
    word_list.sort(key=lambda x: x[1])
    return word_list[:5], word_list[-5:]
