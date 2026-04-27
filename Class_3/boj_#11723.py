'''

비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.

add x: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.
remove x: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.
check x: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)
all: S를 {1, 2, ..., 20} 으로 바꾼다.
empty: S를 공집합으로 바꾼다.

26
add 1
add 2
check 1
check 2
check 3
remove 2
check 1
check 2
toggle 3
check 1
check 2
check 3
check 4
all
check 10
check 20
toggle 10
remove 20
check 10
check 20
empty
check 1
toggle 1
check 1
toggle 1
check 1

'''
from sys import stdin
input = stdin.readline

T = int(input())

S = set()

for i in range(T):
    command = input()

    if command == "all\n":
        S = {i for i in range(1, 21)}

    elif command == "empty\n":
        S = set()

    else:
        command, n = command.split()
        n = int(n)

        if command == "add":
            S.add(n)

        elif command == "remove":
            if n in S:
                S.remove(n)
            else:
                continue

        elif command == "check":
            if n in S:
                print(1)
            else:
                print(0)

        elif command == "toggle":
            if n in S:
                S.remove(n)
            else:
                S.add(n)

        elif command == "empty":
            S = set()

