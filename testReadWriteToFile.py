import sys

print("Write to the standard output.")
print(sys.stdout.write("Write to the standard output.\n"))
# s = sys.stdin.readline()
# print(s)

print('_____________')

f = open("outfile.txt", 'w')
sys.stdout = f
sys.stdout.writelines(["A first line.\n", "A second line.\n"])
print("A line from the print function")
print('ghghghghghksdfjhsdkjhfksdjh')
sys.stdout = sys.__stdout__
f.close()
print('123')

f = open('outfile.txt', 'w')
print('fdfdfdfd', file=f)
f.close()


