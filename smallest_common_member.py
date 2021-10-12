array1 = [ 2, 20, 40]
array2 = [ 2, 5, 10, 40 ]
array3 = [ 2, 4, 5, 10, 20, 30, 40 ]
array4 = [0,1,2,3,4,5,6,7,8,9,10,40]
super_array = [array1, array2, array3, array4]

def get_scm(super_array):

    match_flag = 0

    for iter1 in super_array[0]:
        
        if match_flag != len(super_array)-1:
            
            match_flag = 0

            possible_match = iter1
            
            for index_j in range(1, len(super_array)):
                
                if index_j == match_flag+1:
                    
                    for iter2 in super_array[index_j]:
                        
                        if iter2 == iter1:
                    
                            match_flag+=1
                    
                            break
                    
                        elif iter2 > iter1:
                    
                            break
                
                        else:
                        
                            pass
            
                else:
                    
                    break

        else:

            break

    if match_flag == len(super_array)-1:
        
        return possible_match

    else:

        return None

print(get_scm(super_array)) 
