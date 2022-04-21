# i = 0
# dict = {}
# while i < 3:
#     name = input('Name? ')
#     age = input('age? ')
#     dict[name] = age
#     i += 1
# name = input('Get name:')
# print(dict[name])

# dict = {}
# with open("moby_01_clean.txt") as infile:
#     for line in infile:
#         dict[line] = dict.get(line, 0) + 1
# values = dict.values()
# maxV = max(values)
# minV = min(values)
# max_words = []
# min_words = []
# for key in dict:
#     if dict[key] == maxV:
#         max_words.append(key)
#     elif dict[key] == minV:
#         min_words.append(key)
# print(maxV, max_words)
# print(minV, min_words)

moby_words = []
with open('moby_01_clean.txt') as infile:
    for word in infile:
        if word.strip():
            moby_words.append(word.strip())
word_count = {}
for word in moby_words:
    count = word_count.setdefault(word, 0)
    count += 1
    word_count[word] += 1
word_list = list(word_count.items())
word_list.sort(key=lambda x: x[1])
print("Most common words:")
for word in reversed(word_list[-5:]):
    print(word)
print("\nLeast common words:")
for word in word_list[:5]:
    print(word)
