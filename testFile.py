import os

print(os.getcwd())
print(os.listdir(os.curdir))
print(os.curdir)
# os.chdir('.git')
print(os.getcwd())
print(os.path.join('bin', 'utils', 'disktools'))
print(os.path.expandvars('$HOMEPATH\\temp'))
print(os.curdir)
print(os.pardir)
# print(os.path.isabs(os.path.join(os.pardir, path)))
print(os.listdir(os.curdir))
print(os.name)

if os.name == 'posix':
    root_dir = "/"
elif os.name == 'nt':
    root_dir = "C:\\"
else:
    print("Don't understand this operating system!")
print(root_dir)

import sys

print(sys.platform)
for i in os.environ:
    print(i)

old_path = os.path.abspath('test.log')
print(old_path)
new_path = '{}.{}'.format(old_path, "old")
print(new_path)

import glob

print('__________________')
sum_size = 0
list_txt = glob.glob('*.txt')
for name_file in list_txt:
    file_stats = os.stat(name_file)
    sum_size += file_stats.st_size
print(sum_size)

print('__________________')
import os
for root, dirs, files in os.walk(os.curdir):
    print("{0} has {1} files".format(root, len(files)))
    if ".git" in dirs:
        dirs.remove(".git")
