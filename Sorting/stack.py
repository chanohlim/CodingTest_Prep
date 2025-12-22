'''

탐색: 많은 양의 데이터 중에서 원하는 데이터를 찾는 과정
자료구조: 데이터를 표현하고 관리하고 처리하기 위한 구조

스택: 선입후출(FILO, LIFO) => 팬케이크 쌓기

'''

stack = []

# 삽입(5) - 삽입(2) - 삽입(3) ...

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])