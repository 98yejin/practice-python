def visit(node):
    if node:
        print(node.data)


def inorder(node):
    if node:
        inorder(node.left)
        visit(node)
        inorder(node.right)


def preorder(node):
    if node:
        visit(node)
        preorder(node.left)
        preorder(node.right)


def postorder(node):
    if node:
        postorder(node.left)
        postorder(node.right)
        visit(node)
