

def lightUp(r,c, matrix):
    if r >= 0 and r < len(matrix):
        if c >= 0 and c < len(matrix[r]):
            matrix[r][c] += 1
            #if matrix[r][c] == 10:
                #flash(r,c, matrix)
def flash(r, c, matrix):
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if (not (i == r and j == c)) and (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[r])):
                #print('Flash', r,c, 'light up', i,j)
                lightUp(i, j, matrix)

def getNexts(r, c, matrix):
    nexts = []
    for i in range(r-1, r+2):
        for j in range(c-1, c+2):
            if (not (i == r and j == c)) and (i >= 0 and i < len(matrix) and j >= 0 and j < len(matrix[r])):
                #print('Flash', r,c, 'light up', i,j)
                #ightUp(i, j, matrix)
                nexts.append([i,j])
    return nexts

matrix = []
with open('day_11_test.txt') as file:
    lines = file.read().split('\n')
    for line in lines:
        matrix.append(list(map(int, line)))

for line in matrix:
    print(line)
print('Start')
total_flashes = 0
for step in range(2000):
    # Increase Fields
    flashes = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            matrix[r][c] += 1
            if matrix[r][c] > 9:
                flashes.append([r,c])

 #   for r in range(len(matrix)):
  #      for c in range(len(matrix[r])):
   #         if matrix[r][c] > 9:
    ##            flash(r, c, matrix)
    

    while len(flashes) > 0:
        new_flash = flashes.pop()
        nexts = getNexts(new_flash[0], new_flash[1], matrix)
        for n in nexts:
            matrix[n[0]][n[1]] += 1
            if matrix[n[0]][n[1]] == 10:
                flashes.append(n)
    

    amount_resets = 0
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] > 9:
                total_flashes += 1
                amount_resets += 1
                matrix[r][c] = 0
    if amount_resets == 100:
        print('Ziel erreicht', step)

    #for line in matrix:
    #    print(line)
    #print(step, 'Flashes', total_flashes)
