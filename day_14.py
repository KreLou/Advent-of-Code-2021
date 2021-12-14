

from os import replace


elements = None
combinations = []
with open('day_14_test.txt') as file:
    lines = file.read().split('\n')
    elements = lines[0]
    lines = lines[2:]
    for line in lines:
        parts = line.split(' -> ')
        combinations.append(parts)
print(elements)

for round in range(40):
    replacemenets = []

    for i in range(len(elements)-1):
        substring = elements[i] + elements[i+1]
        #print(i, substring)
        insert = substring
        for combi in combinations:
            if combi[0] == substring:
                insert = combi[0][0] + combi[1]
        replacemenets.append(insert)
    
    elements = ''.join(replacemenets) + elements[-1]
        
    #replacements = [None] * len(elements)
    #for combi in combinations:
    #    if combi[0] in elements:
    #        replace_with = combi[0][0] + combi[1] + combi[0][1]
    #        print(combi[0], '->', replace_with, '(', combi[1],')')
    #        #replacemenets.append([combi[0], replace_with])
    #        replacements[elements.find(combi[0])] = [combi[0], replace_with]
    #print(replacements)

    #for i in range(len(replacements)-1, -1, -1):
    #    combi = replacements[i]
    #    if combi is not None:
    #        elements = elements[:i] + combi[1] + elements[i+2:]
    #        print(combi, elements)
    #        #elements = elements.replace(combi[0], combi[1])

    print('Round', str(round).ljust(4), len(elements))

chars = list(dict.fromkeys(list(elements)))
min = 100000
max = 0
for c in chars:
    amount = elements.count(c)
    if amount > max:
        max = amount
    if amount < min:
        min = amount
print('max:', max)
print('min:', min)
print('dif:', max-min)