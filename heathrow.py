temperatures = []
with open('lab_05.txt') as infile:
    for row in infile:
        temperatures.append(float(row.strip()))
        temperatures.sort()
print('max: ', max(temperatures))
print('min: ', min(temperatures))
print('average: {:.2f}'.format(sum(temperatures) / len(temperatures)))
print('median: ', temperatures[len(temperatures) // 2])
print('count: ', len(temperatures))
print('unic: ', len(set(temperatures)))
