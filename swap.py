def swap(li, first, second):
	temp = li[first]
	li[first] = li[second]
	li[second] = temp

	return li