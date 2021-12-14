



with open('day_10_test.txt') as file:

    lines = file.read().split('\n')

    points = 0
    score_2 = []
    for line in lines:
        match = ''
        isOccured = False
        for c in line:
            if c in ['(','{','[','<']:
                match += c
            else:
                last = match[-1]
                if (c == ')' and last == '(') or (last == '<' and c == '>') or (last == '{' and c == '}') or (last == '[' and c == ']'):
                    match = match[:len(match)-1]
                else:
                    isOccured = True
                    #print('expect', last, 'got', c)


                    if c == ')':
                        points += 3
                    elif c == '}':
                        points += 1197
                    elif c == ']':
                        points += 57
                    elif c == '>':
                        points += 25137
                    break
                    #print(line, 'Fehler')
                #print('the last of ', match, 'is', last, 'rest', match[:len(match) -1:])
        if isOccured:
            #print(line)
            pass
        else:
            score = 0
            added = ''
            for i in range(len(match), 0, -1):
                if match[i-1] == '(':
                    added += ')'
                    score = score * 5 + 1
                elif match[i-1] == '{':
                    added += '}'
                    score = score * 5 + 3
                elif match[i-1] == '<':
                    added += '>'
                    score = score * 5 + 4
                elif match[i-1] == '[':
                    added += ']'
                    score = score * 5 + 2
                    
            print(line,' > ',match, ' need', added)
            score_2.append(score)
        
    print('part 1: ', points)
    score_2.sort()
    print(score_2)
    print('part 2: ', score_2[round(len(score_2)/2)])