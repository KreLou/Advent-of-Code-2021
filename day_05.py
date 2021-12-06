from collections import Counter

def getCoordinatesPerLine(line):
    parts = line.split(' -> ')
    print(parts)
    x1 = parts[0].split(',')[0]
    y1 = parts[0].split(',')[1]
    x2 = parts[1].split(',')[0]
    y2 = parts[1].split(',')[1]
    #print(x1, y1, ' -> ', x2, y2)

    return producePoints(int(x1), int(y1), int(x2), int(y2))

def producePoints(x1, y1, x2, y2):
    points = {}

    delta_x = x2-x1
    anstieg_x = delta_x / abs(delta_x) if delta_x != 0 else 0

    delta_y = y2 - y1
    anstieg_y = delta_y / abs(delta_y) if delta_y != 0 else 0
    print('Delta x: ', delta_x, 'anstieg_x', anstieg_x, 'delta_y', delta_y, 'anstieg_y', anstieg_y)



    if delta_y == 0 or delta_x == 0 or True:
        for i in range(max(abs(delta_x), abs(delta_y))):
            current_x = int(x1 + anstieg_x * i)
            current_y = int(y1 + anstieg_y * i)
            print(i, current_x, current_y)
            points[str(current_x) + ',' + str(current_y)] = 1

        points[str(x2) + ',' +str(y2)] = 1
        print('-', x2, y2)
    return points



cordMap = Counter({})

with open('day_05_data_test.txt') as file:
    lines = file.read().split('\n')
    print(lines)

    for line in lines:
        coords = getCoordinatesPerLine(line)
        #print('Anzahl Coordinaten: ', len(coords.keys()))
        A = Counter(coords)
        cordMap = cordMap + A

print(cordMap)
more_than_2 = 0
for key in cordMap:
    if cordMap[key] > 1:
        more_than_2 += 1
        print(key)
print('Answer: ', more_than_2)