"""
    二叉树及其遍历方法
"""


from time import time
from typing import List


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def generate_tree() -> Node:
    root = Node(
        val=0,
        left=Node(
            val=1,
            left=Node(
                val=3,
                left=Node(7),
                right=Node(8)
            ),
            right=Node(
                val=4,
                left=Node(9)
            )
        ),
        right=Node(
            val=2,
            left=Node(5),
            right=Node(6)
        )
    )
    
    return root


class ErgodicRecursion:
    def __init__(self) -> None:
        self.queue = []
    
    def front(self, root_node: Node):
        if root_node is None:
            return
        self.queue.append(root_node.val)
        self.front(root_node.left)
        self.front(root_node.right)
    
    def middle(self, root_node: Node):
        if root_node is None:
            return
        self.middle(root_node.left)
        self.queue.append(root_node.val)
        self.middle(root_node.right)
        
    def later(self, root_node: Node):
        if root_node is None:
            return
        self.later(root_node.left)
        self.later(root_node.right)
        self.queue.append(root_node.val)
    
    def __del__(self):
        print(self.queue)
        
if __name__ == "__main__":
    """
    构建一棵树用于遍历
                     0
               1          2
           3      4    5     6
         7  8   9
    """
    root = generate_tree()
    
    start_time = time()
    ErgodicRecursion().front(root)  # [0, 1, 3, 7, 8, 4, 9, 2, 5, 6]
    ErgodicRecursion().middle(root)  # [7, 3, 8, 1, 9, 4, 0, 5, 2, 6]
    ErgodicRecursion().later(root)  # [7, 8, 3, 9, 4, 1, 5, 6, 2, 0]
    print(f"Cost time : {time() - start_time}s")
