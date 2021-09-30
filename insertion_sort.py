a = [1000,21,15,15267,51,1,5,26,62,6,2]
size = len(a)

for index_i in range(1,size):

    temp = a[index_i]

    for index_j in reversed(range(0,index_i)):

        if temp < a[index_j]:

            a[index_j+1] = a[index_j]

            if index_j == 0:

                a[index_j] = temp

            else:

                pass

        elif temp > a[index_j]:

            a[index_j+1] = temp

            break

        else:
            
            pass

print(a)
