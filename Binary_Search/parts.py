'''

동빈이네 전자 매장에는 부품이 N개 있다. 각 부품은 정수 형태의 고유한 번호가 있다.
어느 날 손님이 M개 종류의 부품을 대량으로 구매하겠다며 당일 날 견적서를 요청했다.
동빈이는 때를 놓치지 않고 손님이 문의한 부품 M개 종류를 모두 확인해서 견적서를 작성해야 한다.
이때 가게 안에 부품 이 모두 있는지 확인하는 프로그램을 작성해보자.

예를 들어 가게의 부품이 총 5개일 때 부품 번호가 다음과 같다고 하자.

N = 5
[8, 3, 7, 9, 2]

손님은 총 3개의 부품이 있는지 확인 요청했는데 부품 번호는 다음과 같다.

M = 3
[15, 7, 9]

이때 손님이 요청한 부품 번호의 순서대로 부품을 확인해 부품이 있으면 yes를, 없으면 no를 출력 한다. 구분은 공백으로 한다.

입력 조건:

• 첫째 줄에 정수 N이 주어진다. (1 <= N <= 1.000,000)
• 둘째 줄에는 공백으로 구분하여 N개의 정수가 주어진다. 이때 정수는 1보다 크고 1.000,000 이하이다.
• 셋째 줄에는 정수 M이 주어진다. (1 <= M <= 100,000)
• 넷째 줄에는 공백으로 구분하여 M개의 정수가 주어진다. 이때 정수는 1보다 크고 1,000,000 이하이다.

출력 조건:

• 첫째 줄에 공백으로 구분하여 각 부품이 존재하면 yes를, 없으면 no를 출력한다.


입력 예시:
5
8 3 7 9 2
3
5 7 9

출력 예시:
no yes yes

'''

# 입력 부분

N = int(input())
parts = list(map(int, input().split()))

M = int(input())
search = list(map(int, input().split()))

def binary_search(arr, target, start, end):

    if start > end:
        return "no"

    mid = (start + end) // 2 # while문 밖에 있어도 괜찮기는 함, 다만 start가 end보다 크면 이 연산을 수행할 필요가 없기 때문

    if arr[mid] == target:
        return "yes"
            
    if arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    
    elif arr[mid] < target:
        return binary_search(arr, target, mid + 1, end)
        
    
for i in search:
    print(binary_search(parts, i, 0, len(parts) - 1), end = ' ')