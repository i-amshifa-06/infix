class Node: 
    def __init__(s,d): s.data,d; s.left=s.right=None
def insert(r,d):
    if r is None: return Node(d)
    if d<r.data:r.left=insert(r.left,d)
    else:r.right=insert(r.right,d)
    return r
def inorder(r): 
    if r: inorder(r.left); print(r.data,end=' '); inorder(r.right)
root=None
for x in [50,30,70,20,40,60,80]: root=insert(root,x)
inorder(root)