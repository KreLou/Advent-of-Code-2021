def part1(lines):
    total = 0
    for line in lines:
        output = line.replace('\n', '').split('|')[1]
        digits = output.split(' ')
        for digit in digits:
            if 'a' in digit or 'e' in digit or 'f' in digit or 'b' in digit or 'c' in digit or 'd' in digit or 'g' in digit:
                if len(digit) in [2, 3, 4, 7]:
                    total += 1

    return total


class Segment:
    middle_line = None # filled by 3
    lower_line = None # filled by 9
    bottom_left = None # filled by 9
    top_right = None # filled by 6

    def checkIs2(self, digit, mapping):
        if self.top_right is None or self.bottom_left is None:
            return False
        rev_map = {str(v): k for k, v in mapping.items()}
        if not '9' in rev_map.keys():
            return False

        combine = rev_map['9'].replace(self.top_right, '') + self.bottom_left
        print('Suche 6:', combine, digit)
        if len(combine) == len(digit):
            for d in combine:
                if d not in digit:
                    return False
            return True
        else:
            return False

    def checkIs3(self, digit, mapping):
        rev_map = {str(v): k for k, v in mapping.items()}
        if self.lower_line is None or self.bottom_left is None:
            return False

        combine = rev_map['7'] +self.lower_line
        combine = "".join(set(combine))

        if len(digit) == len(combine) + 1:
            for d in combine:
                if d not in digit:
                    return False

            if self.bottom_left in digit:
                return False
            
            for d in digit:
                if d not in combine:
                    self.middle_line = d
            return True
        else:
            return False

    def checkIs5(self, digit, mapping):
        if self.bottom_left is None:
            return False
        rev_map = {str(v): k for k, v in mapping.items()}
        if not '6' in rev_map.keys():
            return False

        combine = rev_map['6'].replace(self.bottom_left, '')
        if len(combine) == len(digit):
            for d in combine:
                if d not in digit:
                    return False
            return True
        else:
            return False

    def checkIs6(self, digit, mapping):
        rev_map = {str(v): k for k, v in mapping.items()}
        if '9' in rev_map.keys() and '0' in rev_map.keys():
            if len(digit)  == len(rev_map['9']):
                for d in rev_map['9']:
                    if d not in digit:
                        self.top_right =d
                return True

            else:
                return False
        else:
            return False

    def checkIs9(self, digit, mapping):
        rev_map = {str(v): k for k, v in mapping.items()}
        combine = rev_map['4'] + rev_map ['7']
        combine = "".join(set(combine))
        if len(combine) +1 == len(digit):
            for d in combine:
                if d not in digit:
                    return False
            for d in digit:
                if d not in combine:
                    self.lower_line = d

            for d in rev_map['8']:
                if d not in digit:
                    self.bottom_left = d
            return True
        else:
            return False
    
    def checkIs0(self, digit, mapping):
        if self.middle_line is None:
            return False
        rev_map = {str(v): k for k, v in mapping.items()}
        combine = rev_map['8'].replace(self.middle_line, '')

        if len(combine) == len(digit):
            for d in combine:
                if d not in digit:
                    return False

            return True
        else:
            return False



total = 0
with open('day_08_data.txt') as file:
    lines = file.readlines()


    for line in lines:
        segment = Segment()
        inputs = line.split('|')[0]
        output = line.replace('\n', '').split('|')[1][1:]
        output_digits = output.split(' ')
        input_digits = inputs.split(' ')

        mapping = {}

        # Zuweisung der Bekannten
        for digit in input_digits:
            if len(digit) == 2:
                mapping[digit] = 1
            elif len(digit) == 4:
                mapping[digit] = 4
            elif len(digit) == 3:
                mapping[digit] = 7
            elif len(digit) == 7:
                mapping[digit] = 8
        
        # Zuweisung der Unbekannten in 6 Iterationen (+ 1 zur Sicherheit)
        for i in range(7):
            for digit in input_digits:
                if digit not in mapping.keys() and len(digit) > 0:
                    if segment.checkIs9(digit, mapping):
                        mapping[digit] = 9
                    elif segment.checkIs3(digit, mapping):
                        mapping[digit] = 3
                    elif segment.checkIs6(digit, mapping):
                        mapping[digit] = 6
                    elif segment.checkIs0(digit, mapping):
                        mapping[digit] = 0
                    elif segment.checkIs5(digit, mapping):
                        mapping[digit] = 5
                    elif len(mapping.keys()) == 9: # Keine Bildungsregel gefunden -> Ausschlussverfahren
                        mapping[digit] = 2
                        i = 100 # Abbruch
                    

        sorted_mapping = {}
        for key, value in mapping.items():
            sorted_key = "".join(sorted(key))
            sorted_mapping[sorted_key] = value

        line_total = 0
        for i in range(len(output_digits)):

            factor =10**(len(output_digits) -i - 1)
            sorted_digit = "".join(sorted(output_digits[i]))
            value = sorted_mapping[sorted_digit]
            line_total += value * factor
        total += line_total
    print('Part 1:', part1(lines))
print('Part 2:', total)