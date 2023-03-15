from multiprocessing.sharedctypes import Value
from dataclasses import dataclass

@dataclass
class TreeNode:
    value:int 
    left:'TreeNode'= None
    right:'TreeNode' = None

    def __repr__(self):
        return str(self.value)

    def __post_init__(self):
        if self.left and self.right is not None:
            if self.left.value > self.value or self.right.value < self.value:
                raise ValueError('value error')

def search(value_to_find:int, node)->int or None:
    if node is None or node.value == value_to_find:
        return node
    
    elif node.value < value_to_find:
        return search(value_to_find, node.right)
    
    elif node.value > value_to_find:
        return search(value_to_find, node.left)

    else:
        raise ValueError('value does not exist')

def insert(value_to_insert:int, node):
    if node.value < value_to_insert:
        if node.right is None:
            node.right = TreeNode(value_to_insert)
        else:
            insert(value_to_insert, node.right)
    elif node.value > value_to_insert:
        if node.left is None:
            node.left = TreeNode(value_to_insert)
        else:
            insert(value_to_insert, node.left)

def lift(node:TreeNode, node_to_delete):
    if node.left:
        node.left = lift(node.left, node_to_delete)
        return node
    else:
        node_to_delete.value = node.value
        return node.right
    
def delete(value_to_delete:int, node:TreeNode):
    if node is None:
        return None

    elif node.value < value_to_delete:
        node.right = delete(value_to_delete, node.right)
        return node

    elif node.value > value_to_delete:
        node.left = delete(value_to_delete, node.left)
        return node
    
    elif node.value == value_to_delete:
        if node.left is None:
            return node.right
        elif node.right is None:
            return node.left
        else:
            node.right = lift(node.right,node)
            return node

if __name__ == "__main__":
    node_1 = TreeNode(25)
    node_2 = TreeNode(75)
    root_node = TreeNode(value=50, left=node_1, right=node_2)
    print(root_node)

    # search
    print(search(25, root_node))

    # insertion
    insert(30, root_node)
    print(search(30, root_node))
    insert(11, root_node)
    insert(61, root_node)
    insert(33, root_node)
    insert(89, root_node)
    insert(30, root_node)
    insert(40, root_node)
    insert(52, root_node)
    insert(82, root_node)
    insert(95, root_node)

    # deletion
    delete(25, root_node)

    # check that 95 is to the right of 89
    assert search(89, root_node).right.value == 95
    
    delete(89, root_node)
    print(search(95, root_node))