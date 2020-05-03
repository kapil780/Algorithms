a = [102,21,23,2,24,1,24,54,3]
def mergeSort(array):
	if len(array) > 1:
		mid = len(array) // 2
		L_side = array[:mid]
		R_side = array[mid:]
		mergeSort(L_side)
		mergeSort(R_side)

		i = j = k = 0

		while i < len(L_side) and j < len(R_side):
			if L_side[i] < R_side[j]:
				array[k] = L_side[i]
				i += 1
			else:
				array[k] = R_side[j]
				j += 1
			k += 1

		while i < len(L_side):
			array[k] = L_side[i]
			i += 1
			k += 1
		while j < len(R_side):
			array[k] = R_side[j]
			j += 1
			k += 1

mergeSort(a)
print(a)