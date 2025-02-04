array = [7,5,9,0,3,1,6,2,4,8]

n = len(array)

# for i in range(1,n):
#     j = i - 1
#     while (array[i] < array[j]):
#         array[i], array[j] = array[j], array[i]
#         if(i > 1):
#             i -= 1
#             j = i - 1

for i in range(1, n):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)