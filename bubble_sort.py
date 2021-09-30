a = [15,51,1,5,26,62,6,2]
size = len(a)

for iteration in range(0, size-2):
    for index in range(0, size-1):
        if a[index] > a[index+1]:
            a[index],a[index+1] = a[index+1],a[index]
        else:
            pass

print(a)
