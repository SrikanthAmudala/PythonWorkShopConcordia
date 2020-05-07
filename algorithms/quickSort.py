

def quickSort(x, index, pivot_index_original):
	pivot_index = pivot_index_original
	if index >= pivot_index:
		return x	

	while pivot_index > index:
		if x[index] > x[pivot_index]:
			appendElement = x[index]   
			x[index] = x[pivot_index-1] 
			x[pivot_index-1] = x[pivot_index]
			x[pivot_index] = appendElement
			pivot_index -=1
		else:
			index+=1
	quickSort(x, 0, pivot_index-1)
	quickSort(x, pivot_index+1, pivot_index_original)
	return x

def recursiveQuickSort(index, pivot_index):
	if index < pivot_index:
		j = quickSort(index, pivot_index)
		recursiveQuickSort(index, j-1)
		recursiveQuickSort(j+1, pivot_index)

x = [6, 5, 8, 9, 3, 10, 15, 12, 16]

pivot_index = len(x)-1
index = 0
quickSort(x, index, pivot_index)
print(x)