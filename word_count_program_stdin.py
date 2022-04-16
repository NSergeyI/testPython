import sys
from argparse import ArgumentParser


def main():
    char_count = 0
    option = 'r'

    parser = ArgumentParser()
    parser.add_argument("-c", "--char", help="num char", action="store_true")
    parser.add_argument("-s", "--symbol", help="num symbol", action="store_true")
    parser.add_argument("file_data", help="read data from this file", action="store_false")
    args = parser.parse_args()
    if args.char:
        option = 'rb'
    elif args.symbol:
        option = 'r'
    if args.file_data:
        infile = open(args.file_data, option)
    else:
        infile = sys.stdin
    with infile:
        for line in infile:
            char_count += len(line)
    print('count {}'.format(char_count))


if __name__ == '__main__':
    main()
