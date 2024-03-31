unsorted_tuple = [(3, 5), (1, 4), (2, 1)]

sorted_tuple = sorted(unsorted_tuple, key=lambda x: x[0])

print(sorted_tuple)