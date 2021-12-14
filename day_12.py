def canGoToSmallCaveAgain(cave, path):
    for i in range(len(path)):
        if path[i].islower():
            for j in range(i+1, len(path)):
                if path[j].islower():
                    if path[i] == path[j]:
                        #print('Cant go to', cave, 'visit', path[i], path[j])
                        return False
    #print('Can go to', cave)
    return True


def findFurtherWays(current_position, connections, way):
    possible_ways = []
    for option in connections:
        if option[0] == current_position and option[1] != 'start':
            #print('Find way for', current_position, option)
            if option[1] == 'end':
                #print('Find end')
                new_way = way.copy()
                new_way.append(option[1])
                possible_ways.append(new_way)

            elif option[1].isupper():
                #print(' > Upper', option[1],way)
                new_way = way.copy()
                new_way.append(option[1])
                possible_ways.append(new_way)
            
            #elif option[1] not in way:
            elif option[1] not in way or (option[1].islower and canGoToSmallCaveAgain(option[1], way)):
                #print(' > Lower', option[1],way)
                new_way = way.copy()
                new_way.append(option[1])
                possible_ways.append(new_way)
    return possible_ways


connections = []
with open('day_12_test.txt') as file:
    lines = file.read().split('\n')
    for line in lines:
        caves = line.split('-')
        connections.append(caves)
        if caves[0] != 'start' and caves[1] != 'end':
            connections.append([caves[1], caves[0]])

print(connections)

options = findFurtherWays('start', connections, ['start'])

allPathsEnds = False
while allPathsEnds == False:
    allPathsEnds = True
    working_options = []
    for option in options:
        pos = option[len(option)-1]
        if pos == 'end':
            working_options.extend([option])
        else:
            allPathsEnds = False
            ways = findFurtherWays(pos, connections, option)
            working_options.extend(ways)
    #print('Find options: ', working_options)
    options = working_options
 
for option in options:
    #print(option)
    print(' > '.join(option))
print(len(options), 'Paths')