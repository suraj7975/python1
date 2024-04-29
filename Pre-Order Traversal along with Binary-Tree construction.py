class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order_traversal(root):
    res = []
    if root:
        res.append(root.val)
        res = res + pre_order_traversal(root.left)
        res = res + pre_order_traversal(root.right)
    return res


root = Node(11)
root.left = Node(7)
root.left.left = Node(5)
root.left.left.left = Node(3)
root.left.right = Node(9)
root.left.right.left = Node(8)
root.left.right.right = Node(10)
root.right = Node(15)
root.right.left = Node(13)
root.right.left.left = Node(12)
root.right.left.right = Node(14)
root.right.right = Node(20)
root.right.right.left = Node(18)
root.right.right.right= Node(25)




print(*pre_order_traversal(root))
