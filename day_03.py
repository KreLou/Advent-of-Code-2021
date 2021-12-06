

with open('day_03_data.txt') as file:
    lines = file.readlines()
    print(len(lines), 'Zeilen')

    max_numbers = 5


    gamma = {}
    epsilon = {}
    for i in range(max_numbers):
        gamma[i] = 0
        epsilon[i] = 0


    for line in lines:
        for i in range(max_numbers):
            gamma[i] += int(line[i])

    print(gamma)

    for i in range(max_numbers):
        gamma[i] = 0 if gamma[i] < len(lines) / 2 else 1
        epsilon[i] = 0 if gamma[i] == 1 else 1
    
    print(gamma)

    gamma_sum = 0
    for key in gamma:
        gamma_sum += 2**key * gamma[key]

    epsilon_sum = 0
    for key in epsilon:
        epsilon_sum += 2**key * epsilon[key]
    
    print('Total: ', gamma_sum * epsilon_sum)