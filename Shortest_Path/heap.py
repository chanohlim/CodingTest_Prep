'''

힙: 완전 이진 트리, 배열로 표현, 부모 <= 자식이 항상 성립한다

완전 이진 트리이므로 탐색 알고리즘의 시간 복잡도가 O(logn)으로 보장된다.


힙을 구현할 때는 배열(리스트)로 구현



노드 - 인덱스

부모:
(i - 1) // 2

왼쪽 자식:
2*i + 1

오른쪽 자식:
2*i + 2

예) 
0: 루트 노드 - 자식: 1, 2

1: 부모: 0, 자식: 3, 4
2: 부모: 0, 자식: 5, 6
3: 부모: 1, 자식: 7, 8
4: 부모: 1, 자식: 9, 10
5: 부모: 2, 자식: 11, 12
6: 부모: 2, 자식: 13, 14
.
.
.


'''

class MinHeap:

    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1) # 새 값은 항상 배열의 맨 끝에 들어감

    
    def pop(self):
        if not self.heap: # 만약 heap 속성, 즉 리스트가 비어있다면 None 반환
            return None
        
        if len(self.heap) == 1: # 만약 원소가 한 개라면, pop 해서 바로 반환
            return self.heap.pop()
        
        root = self.heap[0] # 만약 모두 아니라면, heap 리스트의 첫 원소가 root 값
        self.heap[0] = self.heap.pop() # 마지막 원소를 root로 올림
        self._heapify_down(0) # 방금 가져온 마지막 원소에서 heapify down(재정렬 함수) 호출
        return root # 루트 값(가장 우선순위가 높은 값) 반환


    def _heapify_up(self, idx): # push 메서드 호출 시 노드가 알맞은 위치에 찾아갈 수 있도록 조정
        parent = (idx - 1) // 2 # 부모 노드는 현재 idx 값의 부모 노드 값
        while idx > 0 and self.heap[idx] < self.heap[parent]: # 루트(0번 인덱스)면 멈춘다, 최소 힙 조건(부모가 자식보다 작음) 위반 시 swap
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2 # 위반 시, 자식 노드와 parent 노드의 위치를 swap하고, idx값을 parent 노드의 값, parent 값도 초기화

    def _heapify_down(self, idx): # pop 메서드 호출 시 이진 트리 재정렬
        left = idx * 2 + 1 # idx의 왼쪽 자식 인덱스 계산
        right = idx * 2 + 2 # idx의 오른쪽 자식 인덱스 계산
        smallest = idx # 최소 힙의 조건에 따라 부모 노드가 최솟값이라 가정

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]: # 왼쪽 자식이 존재하고, 왼쪽 자식 노드가 부모 노드보다 작으면
            smallest = left # 최솟값의 인덱스가 왼쪽 자식의 인덱스로 설정
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]: # 오른쪽 자식이 존재하고, 오른쪽 자식 노드가 부모 노드보다 작으면
            smallest = right # 최솟값의 인덱스가 오른쪽 자식의 인덱스로 설정

        if smallest != idx: # 만약 위의 두 if 문 중에 걸린 것 (최소 힙 위반)이 있다면
            self.heap[idx], self.heap[smallest] = self.heap[smallest], self.heap[idx] # 부모 노드와 자식 노드 위치 스왑 => 부모 노드에 자식 노드가 들어가고, 자식 노드에 부모 노드가 들어감
            self._heapify_down(smallest) # 자식 노드의 인덱스를 매개로 전달하는 heapify_down 함수를 재귀 호출 => 인덱스가 heap 크기를 넘어설 때까지 or heap 조건에 위반되지 않을 때가지 반복

    def print_tree(self):
        n = len(self.heap)
        if n == 0:
            print("(empty)")
            return

        height = (n - 1).bit_length()
        max_width = 2 ** height * 2

        idx = 0
        level = 0

        while idx < n:
            level_count = 2 ** level
            nodes = self.heap[idx:idx + level_count]

            # 🔽 (priority, node) → node만 추출
            display_nodes = [str(node[1]) for node in nodes]

            space_between = max_width // (level_count + 1)
            line = " " * (space_between // 2)
            line += (" " * space_between).join(display_nodes)
            print(line)

            # 가지 출력
            if idx + level_count < n:
                branch_line = ""
                for _ in display_nodes:
                    branch_line += " " * (space_between // 2 - 1)
                    branch_line += "/"
                    branch_line += " " * 3
                    branch_line += "\\"
                    branch_line += " " * (space_between // 2 - 1)
                print(branch_line)

            idx += level_count
            level += 1


h = MinHeap()
h.push((3, 'A'))
h.push((1, 'B'))
h.push((2, 'C'))
h.push((0, 'D'))
h.push((8, 'H'))
h.push((6, 'K'))

h.print_tree()

h.pop()
h.print_tree()