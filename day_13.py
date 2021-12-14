def printPaper(paper):
    for line in paper:
        print(''.join(line))
def createPaper(x, y):
    paper = []
    for i in range(y ):
        paper.append(['.']*(x))
    return paper

cords = []
folds = []
max_lines = 0
max_columns = 0
with open('day_13_test.txt') as file:
    lines = file.read().split('\n')
    for line in lines:
        if line.startswith('fold'):
            instruction = line.split('=')
            folds.append([instruction[0][-1], int(instruction[1])])
        elif ',' in line:
            inst = line.split(',')
            cords.append([int(inst[0]), int(inst[1])])
            max_lines = max(max_lines, int(inst[1]))
            max_columns = max(max_columns, int(inst[0]))

paper = createPaper(max_columns+1, max_lines+1)

for cord in cords:
    paper[cord[1]][cord[0]] = '#'
printPaper(paper)

for fold in folds:
    if fold[0] == 'y':
        print('Fold on y=', fold[1])
        paper[fold[1]] = ['-']*len(paper[fold[1]])
        new_paper_height = max(len(paper) - fold[1]-1, fold[1])
        #print('new paper height: ', new_paper_height)
        new_paper = createPaper(len(paper[0]), new_paper_height)

        for i in range(len(new_paper)):
            i_old_1 = i
            i_old_2 = len(paper) - i - 1
            for c in range(len(paper[0])):
                if paper[i_old_1][c] == '#' or paper[i_old_2][c] == '#':
                    new_paper[i][c] = '#'
        #print('After Fold:')
        #printPaper(new_paper)
        paper = new_paper
    if fold[0] == 'x':
        print('Fold on x=', fold[1])
        for i in range(len(paper)):
            paper[i][fold[1]] = '|'
        new_paper_width = max(len(paper[0]) - fold[1]-1, fold[1])
        #print('new paper width: ', new_paper_width)
        new_paper = createPaper(new_paper_width, len(paper))
        
     
        for row in range(len(new_paper)):
            for c in range(new_paper_width):
                c_old_1 = c
                c_old_2 = len(paper[0]) - c - 1
                if paper[row][c_old_1] == '#' or paper[row][c_old_2] == '#':
                    new_paper[row][c] = '#'

        #print('After Fold:')
        #printPaper(new_paper)
        paper = new_paper

    # Cound
    amount = 0
    for r in paper:
        for c in r:
            if c == '#':
                amount += 1
    print('Found total', amount, '#')
printPaper(paper)