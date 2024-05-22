class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)
    elif key > root.val:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp
        elif root.right is None:
            temp = root.left
            root = None
            return temp
        
        temp_val = find_min_node(root.right)
        
        root.val = temp.val
        
        root.right = delete_node(root.right, temp_val)
            
    return root

def find_min_node(node):
    min_val = node
    while node.left:
        min_val = node.left
    return min_val
    