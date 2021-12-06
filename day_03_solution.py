import numpy as np
import pandas as pd

path = './day_03_data.txt'

line_list = []
with open(path) as file:
	for line in file:
		line = line.strip('\n')
		line_list.append(list(line))

	matrix = np.array(line_list)
	matrix = matrix.astype(np.int32)

	# Part 1
	def find_most_common(matrix):
		matrix_tmp =matrix.copy()
		matrix_tmp[matrix_tmp == 0] = -1
		matrix_sum = matrix_tmp.sum(axis=0)
		matrix_sum[matrix_sum >= 0] = 1
		matrix_sum[matrix_sum < 0] = 0

		return matrix_sum

	matrix_sum = find_most_common(matrix)

	def dataframe_to_int(matrix_row, bitflip=False):
		value = 0
		for idx in range(0, len(matrix_row)):
			bit = matrix_row[len(matrix_row) - idx - 1]
			if bitflip:
				value += 2 ** idx * (1 - bit)
			else:
				value += 2 ** idx * bit
		return value

	gamma_rate = dataframe_to_int(matrix_sum)
	epsilon_rate = dataframe_to_int(matrix_sum, bitflip=True)

	power_consumption = gamma_rate * epsilon_rate
	print(power_consumption)

	# Part 2
	def delete_other_values(matrix, most_common = True):
		matrix = pd.DataFrame(matrix)

		for idx in range(0, matrix.shape[1]):

			matrix_sum = find_most_common(matrix)
			bit = matrix_sum[idx]

			if not most_common:
				bit = 0 if bit else 1

			matrix.drop(matrix.index[matrix[idx] == bit], inplace = True)

			if matrix.shape[0] == 1:
				break

		return matrix
	oxy = delete_other_values(matrix)
	carb = delete_other_values(matrix, most_common=False)

	oxy_int = dataframe_to_int(oxy.to_numpy()[0])
	carb_int = dataframe_to_int(carb.to_numpy()[0])

	print(oxy_int * carb_int)