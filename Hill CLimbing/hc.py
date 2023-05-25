def swapPositions(list, pos1, pos2):
       val1=list[pos1]
       val2=list[pos2]
       list[pos1]=val2
       list[pos2]=val1

       return list


def calculate_heuristic(arr):
    arr_size=len(arr)
    heuristic=0
    
    for i in range (0,arr_size-1):
       for j in range (i+1, arr_size):
          if arr[j]<arr[i]:
            heuristic+=1
            

    return heuristic



arr=[7, 1, 9, 0, 5, 8, 4, 2, 10, 0, 20]
arr_size=len(arr)
result_arr=arr.copy()
lowest_heuristic=calculate_heuristic(arr)
initial_heuristic=lowest_heuristic


while True:
  for i in range (0,arr_size-1):
   for j in range (i+1, arr_size):
    temp_arr=arr.copy()
    swapPositions(temp_arr,i,j)
    heuristic=calculate_heuristic(temp_arr)
    
    if heuristic<lowest_heuristic:
      lowest_heuristic=heuristic
      result_arr=temp_arr.copy()

  if lowest_heuristic<initial_heuristic and lowest_heuristic>0 :
    arr=result_arr.copy() 
  else:  
    break

print("lowest heuristic :")
print(lowest_heuristic)
print("Result array: ")
print(result_arr) 