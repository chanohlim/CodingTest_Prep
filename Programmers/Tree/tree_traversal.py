def preorder(nodes, idx):

    if idx < len(nodes):
        # 부모 => 왼쪽 자식 => 오른쪽 자식
        ret = str(nodes[idx]) + " "
        ret += preorder(nodes, idx*2 + 1)
        ret += preorder(nodes, idx*2 + 2)
        return ret

    else:
        return ''

def inorder(nodes, idx):

    if idx < len(nodes):

        ret = inorder(nodes, idx*2 + 1)
        ret += str(nodes[idx]) + ' '
        ret += inorder(nodes, idx*2 + 2)

        return ret

    else:
        return ''

def postorder(nodes, idx):

    if idx < len(nodes):

        ret = postorder(nodes, idx*2 + 1)
        ret += postorder(nodes, idx*2 + 2)
        ret += str(nodes[idx]) + ' '

        return ret
    
    else:
        return ''


def solution(nodes):

    return[
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1]
    ]


nodes = [1,2,3,4,5,6,7]
print(solution(nodes))