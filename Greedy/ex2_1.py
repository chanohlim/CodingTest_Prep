'''
첫째 줄에 N(2 <= N <= 1000), M(1 <= M <= 10,000), K(1 <= K <= 10,000)의
자연수가 주어지며, 각 자연수는 공백으로 구분한다.

둘째 줄에 N개의 자연수가 주어진다. 각 자연수는 공백으로 구분한다. 단, 각각의 자연수는
1 이상 10,000 이하의 수로 주어진다.

입력으로 주어지는 K는 항상 M보다 작거나 같다.

입력:
5 8 3
2 4 5 4 6

출력:
46
'''

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

largest,index = 0,0

for i in range(n):
    if data[i] >= largest:
        largest = data[i]
        index = i

data[index] = 0

large, index = 0,0

for i in range(n):
    if data[i] >= large:
        large = data[i]
        index = i
    
print( (largest*(m//(k+1))*k), (large*(m//(k+1))), (largest*(m%(k+1))) )
    

'''

5 8 3
666 5 666 5 / 8 => m // k+1 => 2
666 5 666 5 666 5 66 / 14 => 3
666 5 666 5 6 ==> 9 => 2
666 5 666 5 666 5 666
n, m, k = map(int, input().split(' '))
data = list(map(int, input().split(' ')))

data.sort()
max1 = data[n-1]
max2 = data[n-2]

count = int(m / (k+1) )*k + m % (k+1)

sum = max1 * count + max2 * (m-count)

print(sum)
'''