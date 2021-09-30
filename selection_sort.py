a = [1000,21,15,15267,51,1,5,26,62,6,2]
size = len(a)

def find_minima_index(a, start_index, size):
    minima = a[start_index]
    minima_index = start_index
    for index in range(start_index+1, size):
        if a[index] < minima:
            minima = a[index]
            minima_index = index
        else:
            pass

    return minima_index

for index in range(0, size):

    minima_index = find_minima_index(a, index, size)

    if a[index] > a[minima_index]:
        a[index],a[minima_index] = a[minima_index],a[index]
    else:
        pass


print(a)
