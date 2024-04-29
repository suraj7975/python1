n=int(input())
l=list(map(int,input().split()))
index=int(input())
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
        
def insertIntoBST(root,value):
    if root==None:
        newnode=TreeNode(value)
        return newnode

    if root.data>value:
        root.left=insertIntoBST(root.left,value)
    else:
        root.right=insertIntoBST(root.right,value)
    return root

def fillInOrder(inorder,root):
    if root==None:
        return
    fillInOrder(inorder,root.left)
    inorder.append(root.data)
    fillInOrder(inorder,root.right)

root=None
for ele in l:
    root=insertIntoBST(root,ele)
k=index
inorder=[]
fillInOrder(inorder,root)
print(inorder[k-1])
