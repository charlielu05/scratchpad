# Preorder Tree Traversal
root = {'data': 'A', 'children': [{'data': 'B', 'children':
[{'data': 'D', 'children': []}]}, {'data': 'C', 'children':
[{'data': 'E', 'children': [{'data': 'G', 'children': []},
{'data': 'H', 'children': []}]}, {'data': 'F', 'children': []}]}]}

def preOrderTraverse(node):
    print(node['data'], end= ' ')
    if len(node['children']) > 0:
        for child in node['children']:
            preOrderTraverse(child) 
    return 

preOrderTraverse(root)

def postOrderTraverse(node):
    if len(node['children']) > 0:
        for child in node['children']:
            postOrderTraverse(child) 
    print(node['data'], end= ' ')     
    return 

postOrderTraverse(root)

# both depth first search, only difference is in when the data is accessed. 

def inorderTraverse(node):
    if len(node['children']) >= 1:
        # RECURSIVE CASE
        inorderTraverse(node['children'][0])  # Traverse the left child.
    print(node['data'], end=' ')  # Access this node's data.
    if len(node['children']) >= 2:
        # RECURSIVE CASE
        inorderTraverse(node['children'][1])  # Traverse the right child.
    # BASE CASE
    return

inorderTraverse(root)