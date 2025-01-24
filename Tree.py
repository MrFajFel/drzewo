from enum import nonmember

from TreeNode import TreeNode


class Tree:
    def __init__(self,root_value):
        self.root = TreeNode(root_value,None,None,None)


    def read_from_file(self,filename):
        pass

    def add_node(self,node,parent_node):
        if parent_node.left is None:
            parent_node.left = node
        elif parent_node.right is None:
            parent_node.right = node
        else:
            raise Exception("Node is full")

    def dfs_show(self, node):
        print(node.value)
        if node.left is not None:
            self.dfs_show(node.left)
        if node.right is not None:
            self.dfs_show(node.right)
        return


    def bfs_show(self):
        queue = []
        node =  self.root
        while True:
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
            print(node.value)
            try:
                node = queue.pop(0)
            except IndexError:
                break