import fileinput
def main():
    for line in fileinput.input():
        if not line.startswith('##'):
            print(fileinput.filename())
            print(fileinput.lineno())
            print(fileinput.filelineno())
            print(line, end="")
main()