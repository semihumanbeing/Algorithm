class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 

def init_tree():
    global root

    new_node = Node('A')
    root = new_node
    new_node = Node('B')
    root.left = new_node
    new_node = Node('C')
    root.right = new_node

# 노드는 오직 한번만 방문한다.
    
#전위 순회

def preorder(node):
    if node == None: return 
    print(node.data, end = '->')
    preorder(node.left)
    preorder(node.right)

# 중위순회
def inorder(node):
    if node == None: return
    inorder(node.left)
    print(node.data, end = '->')
    inorder(node.right)


# 후위순회
def postorder(node):
    if node == None: return
    inorder(node.left)
    inorder(node.right)
    print(node.data, end = '->')


    