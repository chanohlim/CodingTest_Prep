a = list(map(int, input().split()))

mixed = False
ascending = True

if a[0] == 8:
    for i in range(7):
        if a[i] < a[i+1]:
            mixed = True
            break
    
    ascending = False

elif a[0] == 1:
    for i in range(7):
        if a[i] > a[i+1]:
            mixed = True
            break

else:
    mixed = True

if mixed:
    print('mixed')
else:
    if ascending:
        print('ascending')
    else:
        print('descending')