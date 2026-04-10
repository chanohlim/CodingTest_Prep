'''

4
3
4
1
1

2

4
6
2
2
3
3
4
4

3

'''

G = int(input())
P = int(input())

root = [i for i in range(G + 1)]
planes = []


def bruteforce():

    gate = [0 for i in range(G + 1)]
    airplanes = []

    for i in range(P):
        airplanes.append(int(input()))

    result = 0

    for airplane in airplanes:

        cnt = 0

        for i in range(airplane, 0, -1):
            if gate[i] == 0:
                gate[i] = 1
                cnt += 1
                break

        if cnt == 0:
            break

        result += 1

    return result

def find_root(node):

    if root[node] != node:
        root[node] = find_root(root[node])

    return root[node]

def union(a, b):

    root_a = find_root(a)
    root_b = find_root(b)

    if root_a < root_b:
        root[root_b] = root_a
    else:
        root[root_a] = root_b



def main():

    result = 0

    for i in range(P):
        planes.append(int(input()))

    for plane in planes:
        available = find_root(plane)
        
        if available == 0:
            break

        union(available - 1, available)

        result += 1

    return result

print(main())



