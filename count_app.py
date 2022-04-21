import argparse

""" Читает файл и возвращает количество строк, слов
и символов - по аналогии с утилитой UNIX wc
"""


def counter():
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
    return line_count, word_count, char_count
    # print("File has {0} lines, {1} words, {2} characters".format(line_count, word_count, char_count))


def main():
    parser = argparse.ArgumentParser(usage=__doc__)
    parser.add_argument("-l", "--line", dest="line", action='store_true', default=False, help="Only count line")
    parser.add_argument("-w", "--word", dest="word", action='store_true', default=False, help="Only count word")
    parser.add_argument("-c", "--char", dest="char", action='store_true', default=False, help="Only count char")
    args = parser.parse_args()
    string_result = 'File has'
    if not args.line and not args.word and not args.char:
        string_result = string_result + ' {line} - lines {word} - words {char} - characters'
    else:
        if args.line:
            string_result = string_result + ' {line} - lines'
        if args.word:
            string_result = string_result + ' {word} - words'
        if args.char:
            string_result = string_result + ' {char} - characters'
    result = counter()
    print(string_result.format(line=result[0], word=result[1], char=result[2]))


if __name__ == '__main__':
    main()
