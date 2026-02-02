'''
수 찾기
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	128 MB	343214	113570	74240	31.258%

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

5
4 1 5 2 3
5
1 3 7 9 5

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.

1
1
0
0
1


100,000 * 100,000 > 100,000,000 => O(n^2)는 안됨 => 이진 탐색 사용해야된다!
'''

n = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

m = int(input())
arr2 = list(map(int, input().split()))

def binary_search(arr, target, start, end):

    mid = (start + end) // 2

    if start <= end:
    
        if arr[mid] == target:
            return 1
        
        elif arr[mid] > target:
            return binary_search(arr, target, start, mid - 1)
        
        elif arr[mid] < target:
            return binary_search(arr, target, mid + 1, end)

    return 0

for i in arr2:
    print(binary_search(arr1, i, 0, len(arr1) - 1))
