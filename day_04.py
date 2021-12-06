class Board():

    matrix = None
    def __init__(self, lines):
        self.matrix = []
        for line in lines:
            line = line.replace('  ', ' ')
            if line.startswith(' '):
                line = line[1:]
            line_parts = line.split(' ')
            matrix_line = []
            for part in line_parts:
                matrix_line.append({'key': part, 'checked': False})
            self.matrix.append(matrix_line)
    
    def markNumber(self, inputKey):
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j]['key'] == inputKey:
                    self.matrix[i][j]['checked'] = True
    
    def checkMatrix(self):
        for i in range(len(self.matrix)):
            if self.checkMatrixRow(self.matrix[i]):
                #print('Row ', i, 'is correct')
                return True # Row is correct
        for i in range(len(self.matrix[i])):
            if self.checkMatrixColumn(i):
                #print('Column', i, 'i checked')
                return True
        return False


    def checkMatrixColumn(self, columnID):
        for line in self.matrix:
            if line[columnID]['checked'] == False:
                return False
        return True

    def checkMatrixRow(self, row):
        for i in row:
            if i['checked'] == False:
                return False
        return True
    
    def print(self):
        for line in self.matrix:
            print(line[0]['key'].rjust(2), line[1]['key'].rjust(2), line[2]['key'].rjust(2), line[3]['key'].rjust(2), line[4]['key'].rjust(2))

    def getSumOfUnmarkedNumbers(self):
        current_sum = 0
        for line in self.matrix:
            for number in line:
                if number['checked'] == False:
                    current_sum += int(number['key'])
        return current_sum

boards = []
with open('day_04_boards_test.txt') as file:
#with open('day_04_boards_training.txt') as file:
    content = file.read()
    boards_content = content.split('\n\n')
    for board_content in boards_content:
        
        board = Board(board_content.split('\n'))
        #board.print()
        boards.append({'board': board, 'points': 0})
print( 'Anzahl Boards', len(boards))


#input_numbers = '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1'.split(',') # Training
input_numbers = '42,44,71,26,70,92,77,45,6,18,79,54,31,34,64,32,16,55,81,11,90,10,21,87,0,84,8,23,1,12,60,20,57,68,61,82,49,59,22,2,63,33,50,39,28,30,88,41,69,72,98,73,7,65,53,35,96,67,36,4,51,75,24,86,97,85,66,29,74,40,93,58,9,62,95,91,80,99,14,19,43,37,27,56,94,25,83,48,17,38,78,15,52,76,5,13,46,89,47,3'.split(',')


for number in input_numbers:
        for i in range(len(boards)):
            board = boards[i]
            if board['points'] == 0:
                board['board'].markNumber(number)
                if board['board'].checkMatrix():
                    #board['board'].print()
                    points = board['board'].getSumOfUnmarkedNumbers() * int(number)
                    boards[i]['points'] = points

                    print('Board', str(i).rjust(2), 'wins with number', str(number).rjust(2), 'Points: ', points)