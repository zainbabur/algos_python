a = [1000,21,15,15267,51,1,5,26,62,6,2]


def traverse(a):

    if len(a) <= 1:
        
        return a

    else:

        pivot = a.pop(0)
        less_array = []
        greater_array = []

        for iter in a:
            
            if iter <= pivot:
            
                less_array.append(iter)

            else:
            
                greater_array.append(iter)

    return traverse(less_array) + [pivot] + traverse(greater_array)


print(traverse(a))
