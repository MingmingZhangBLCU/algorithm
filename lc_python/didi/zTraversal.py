'''
给定一个二叉树，返回其节点值的锯齿形层序遍历。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

例如：
给定二叉树 [3,9,20,null,null,15,7],

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''
#103
# z / 锯齿 形 遍历
from ds.BinaryTree import TreeNode,creatTree,leveTraversal
# 层次遍历 + 存储+ 逆转
def zigzagLevelOrder(root:TreeNode):
    if root is None:
        return []
    que = [root]
    ans = []
    line = 0  # 偶正 奇反
    while len(que):
        tmp_que = []  #按照顺序
        ans.append([])
        while len(que):
            node = que.pop()
            ans[line].append(node.x)
            if node.left is not None:
                tmp_que.insert(0,node.left)
            if node.right is not None:
                tmp_que.insert(0,node.right)
        line += 1
        que = tmp_que
    for i in range(1,len(ans)):
        if i%2:
            ans[i].reverse()
    return ans


def zigzagLevelOrder2(root:TreeNode):
    if root is None:
        return []
    que = [root]
    line = 0
    ans = []
    while len(que):
        tmp = []
        new_que = []
        while len(que):  # 按层
            node = que.pop(0)
            if line%2:
                tmp.insert(0,node.x)
            else:
                tmp.append(node.x)
            if node.left is not None:
                new_que.append(node.left)
            if node.right is not None:
                new_que.append(node.right)
        line += 1
        que = new_que
        ans.append(tmp)
    return ans

#nums = [7,9,8,4,3,-1,-1]
nums = [1,2,3,4,-1,-1,5]
root = creatTree(nums,0)
leveTraversal(root)
ans = zigzagLevelOrder2(root)
print(ans)
