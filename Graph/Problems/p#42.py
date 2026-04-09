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

root = [0]
rank = [1 for i in range(G + 1)]


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

def union(a, b):

    root_a = root[a]
    root_b = root[b]

    print(a, root_a, b, root_b)

    if root_a == root_b:
        rank[root_a] += 1

        if rank[root_a] > root_a:
            return False
        
        return True

    if root_a > root_b:

        root[root_b] = root_a
        rank[root_a] += rank[root_b]

        if rank[root_a] > root_a:
            return False
        
        return True
        
    else:
        root[root_a] = root_b
        rank[root_b] += rank[root_a]

        if rank[root_b] > root_b:
            return False
        
        return True
    

    

def main():

    for i in range(P):
        root.append(int(input()))

    result = 0

    for i in range(1, P): # i의 root => root[i]

        if not union(i, i+1):
            break

        result += 1

    return result + 1

print(main())



