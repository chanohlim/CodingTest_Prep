array = [7,5,9,0,3,1,6,2,4,8]
n = len(array)

for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if array[j] < array[min_index]:
            min_index = j

    # temp = array[i]
    # array[i] = min
    # array[min_index] = temp

    array[i], array[min_index] = array[min_index], array[i]

print(array)



