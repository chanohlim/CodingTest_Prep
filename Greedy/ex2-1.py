n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

data.sort()
max1 = data[n-1]
max2 = data[n-2]

count = int(m / (k+1) )*k + m % (k+1)

sum = max1 * count + max2 * (m-count)

print(sum)