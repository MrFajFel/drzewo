from Tree import Tree
from TreeNode import TreeNode

tree = Tree(7)
node1 = TreeNode(5,None,None,tree.root)
tree.add_node(node1,tree.root)

node2 = TreeNode(2,None,None,tree.root)
tree.add_node(node2,tree.root)

node3 = TreeNode(7,None,None,node1)
tree.add_node(node3,node1)

node4 = TreeNode(6,None,None,node1)
tree.add_node(node4,node1)

node5 = TreeNode(3,None,None,node2)
tree.add_node(node5,node2)

tree.dfs_show(tree.root)

print("------------")

tree.bfs_show()