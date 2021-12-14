import itertools

def findNearFields(heat_map, x, y, source_direction): # source: 0 = top, 1 = right, 2 = bottom, 3 = left
    if x < 0 or y < 0:
        return None
    if x >= len(heat_map) or y >= len(heat_map[0]):
        return None

    top =       heat_map[x - 1][y] if x > 0 else -1
    left =      heat_map[x][y-1] if y > 0 else -1
    right =     heat_map[x][y +1] if y < len(heat_map[x]) -1 else -1
    bottom =    heat_map[x+1][y] if x < len(heat_map) -1 else -1

    point = heat_map[x][y]

    total_finds = [[x,y]]
    if point < top and source_direction != 2 and top < 9:
        new_x = x-1
        new_y = y
        #print('go from ', x, y, '(', point, ') to top because its lower', top, '(', new_x, new_y, ')')
        result = findNearFields(heat_map, new_x, new_y, 0)
        if result is not None:
            total_finds.extend(result)

    if point < left and source_direction != 1 and left < 9 :
        new_x = x
        new_y = y-1
        #print('go from ', x, y, '(', point, ') to left because its lower', left, '(', new_x, new_y, ')')
        result = findNearFields(heat_map, new_x, new_y, 3)
        if result is not None:
            total_finds.extend(result)

    if point < bottom and source_direction != 0 and bottom < 9:
        new_x = x+1
        new_y = y
        #print('go from ', x, y, '(', point, ') to bott because its lower', bottom, '(', new_x, new_y, ')')
        result = findNearFields(heat_map, new_x, new_y, 2)
        if result is not None:
            total_finds.extend(result)

    if point < right and source_direction != 3 and right < 9:
        new_x = x
        new_y = y+1
        #print('go from ', x, y, '(', point, ') to rght because its lower', right, '(', new_x, new_y, ')')
        result = findNearFields(heat_map, new_x, new_y, 1)
        if result is not None:
            total_finds.extend(result)
    return total_finds



with open('day_09_test.txt') as file:
    lines = file.readlines()


    heat_map = []
    for line in lines:
        heat = list(line.replace('\n', ''))
        heat_map.append(list(map(int, heat)))


for line in heat_map:
    print(line)



founds = 0
risk = 0
for i in range(len(heat_map)):
    for j in range(len(heat_map[i])):
        top = heat_map[i - 1][j] if  i > 0 else 10000
        left = heat_map[i][j-1] if j > 0 else 10000
        right = heat_map[i][j +1] if j < len(heat_map[i]) -1 else 10000
        bottom = heat_map[i+1][j] if i < len(heat_map) -1 else 10000

        point = heat_map[i][j]

        if point < min(top, left, right, bottom):
            founds += 1
            risk += point + 1
print('risk: ', risk)

######## Part 2
basins = []
for i in range(len(heat_map)):
    for j in range(len(heat_map[i])):
        top = heat_map[i - 1][j] if  i > 0 else 10000
        left = heat_map[i][j-1] if j > 0 else 10000
        right = heat_map[i][j +1] if j < len(heat_map[i]) -1 else 10000
        bottom = heat_map[i+1][j] if i < len(heat_map) -1 else 10000

        point = heat_map[i][j]

        if point < min(top, left, right, bottom):
            #print('Found at', i, j)
            finds = findNearFields(heat_map, i, j, -1)
            finds = [x for x in finds if x is not None]
            finds.sort()
            finds = list(finds for finds,_ in itertools.groupby(finds))
            #print('-> ', len(finds),  finds)
            basins.append(len(finds))

basins.sort(reverse=True)
solution = 1
for i in basins[:3]:
    solution = solution * i
print('Part 2:', solution)