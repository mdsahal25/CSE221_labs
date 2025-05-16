def build_postorder(inorder, preorder):
    if not preorder:
        return []
    root = preorder[0]
    idx = inorder.index(root)
    left_postorder = build_postorder(inorder[:idx], preorder[1:idx+1])
    right_postorder = build_postorder(inorder[idx+1:], preorder[idx+1:])
    return left_postorder + right_postorder + [root]
n = int(input())
inorder = list(map(int, input().split()))
preorder = list(map(int, input().split()))
print(*build_postorder(inorder,preorder))