import sys
# sys.path.append('../queue_and_stack')
# from dll_queue import Queue
# from dll_stack import Stack

# * Should have the methods `insert`, `contains`, `get_max`.
#   * `insert` adds the input value to the binary search tree, adhering to the rules 
#   of the ordering of elements in a binary search tree.
#   * `contains` searches the binary search tree for the input value, returning a 
#   boolean indicating whether the value exists in the tree or not.
#   * `get_max` returns the maximum value in the binary search tree.
#   * `for_each` performs a traversal of _every_ node in the tree, executing the passed-in 
#   callback function on each tree node value. There is a myriad of ways to perform tree traversal; 
#   in this case any of them should work. 


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
       
    # Insert the given value into the tree
    def insert(self, value):
        if self.value is None:
            self.value = value
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
       
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        elif target < self.value:
            return self.left.contains(target) if self.left is not None else False
        else:
            return self.right.contains(target) if self.right is not None else False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach

    #for each is an example of a depth first traversal
    def for_each(self, cb):
        cb(self.value)
        if self.right is not None:
            self.right.for_each(cb)
        if self.left is not None:
            self.left.for_each(cb)

    # iterative for_each:

    # def for_each_iterative(self,cb):
    #     stack = Stack()
    #     stack.push(self) #self equals the root node

    #     while stack.len() > 0:
    #         current_node = stack.pop()
    #         if current_node.right:
    #             stack.push(current_node.right)
    #         if current_node.left:
    #             stack.push(current_node.left)
    #         cb(current_node.value)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal

    # steps:
    # make a stack
    # put root in Stack
    # while stack is not empty
    #  pop the root out of stack = does the current value == the value we are looking for? (if target == value: return)
    #  DO THE THING TO IT!!!!
    #     if left, 
    #         add left to stack
    #     if right, 
    #         add right to stack
    # def print(self, arr):
    #     for i in arr:
    #         print(i)
   
    # def in_order_print(self, node): #this is a specific vocabulary term = research
    #     res = []
    #     if node:
    #         res = self.in_order_print(node.left) #left
    #         print(isinstance(res, object))
    #         res.append(node.value) #root 
    #         res = res + self.in_order_print(node.right) #right
    #         print(res, 'right')
           
    #     return res

        
        
            
            
            
            
       
        # while res.size != 0:
        #     v = res.dequeue()
        #     print(v)
        #     print(res.len())
            # self.in_order_print(node)
            # print(res.storage, "current value in storage cache")
                
                   
        # if self.left is not None:
        #     print(self.value)
        #     # self.left.in_order_print(print(self.value))
        #     # return True
        # else:
        #     pass
            
        # if self:
        #     print(self.value)
        #     self.left.in_order_print(node)
        #     print(self.value)
        #     self.right.in_order_print(node)
           
        # queue = Queue()
        # root_node = self
        # queue.enqueue(root_node)
        # while queue.size > 0:
       
        #     if root_node.left is not None:            
        #         print(root_node.left.value, "left")
        #         root_node.left.in_order_print(node)
        #     if root_node.right is not None:
        #         print(root_node.right.value, "right")
        #         root_node.right.in_order_print(node)
        
       

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
#     def bft_print(self, node):
#         queue = Queue()
#         root_node = self
#         queue.enqueue(root_node)
#         while queue.size > 0:
#             current_root = queue.dequeue()
#             print(current_root.value)
#             if current_root.left is not None:
#                 queue.enqueue(current_root.left)
#             if current_root.right is not None:
#                 queue.enqueue(current_root.right)
    

#     # Print the value of every node, starting with the given node,
#     # in an iterative depth first traversal
#     def dft_print(self, node):
#         stack = Stack()
#         root_node = self
#         stack.push(root_node)
#         while stack.size > 0:
#             current_root = stack.pop()
#             print(current_root.value)
#             if current_root.left is not None:
#                 stack.push(current_root.left)
#             if current_root.right is not None:
#                 stack.push(current_root.right)


        

#     # STRETCH Goals -------------------------
#     # Note: Research may be required

#     # Print In-order recursive DFT
#     def pre_order_dft(self, node):
#         pass

#     # Print Post-order recursive DFT
#     def post_order_dft(self, node):
#         pass

# bst = BinarySearchTree(1)
# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)
# print(bst.dft_print(1), "dft_print")
# print(bst.bft_print(1), "bft_print")
# print(bst.in_order_print(bst), "in order print")

# .. the BinarySearchTree is initialized with a root
# t = BinarySearchTree(6)
# t.insert(5)
# t.queue.storage.get_cache()
# t.insert(7)
# t.queue.storage.get_cache()
# t.insert(8)
# t.queue.storage.get_cache() 

# b = BinarySearchTree(5)
# b.insert(10)
# b.insert(4)
# b.insert(2)
# b.insert(7)
# print(b.dft_print(10), "dft_print")
# print(b.bft_print(10), "bft_print")

#https://www.geeksforgeeks.org/binary-search-tree-data-structure/

# binary search is O(log n) (worst case O(n))- because every step you divide by half, you remove half of the things
# in a binary search tree you don't care about the right side of the tree until you are finished with the left
# or vice versa

# https://www.cs.usfca.edu/~galles/visualization/BST.html
# https://visualgo.net/en/bst?slide=1

# when can a Binary tree be O(n)? when the tree is imbalanced and an arm of it is all in a row

# returns the first instance of a value in a tree

# When a programmer says big o.. they often are referring to the avg, which is THETA

#deleting the root, reorder = find the largest of the smallest , which will keep the tree balanced

#Rule: every child in a binary search tree (BST) is also a BST
#Rule: if greater than or equal too, go right 

# class BinarySearchTree:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#         self.queue = Queue()

#     # Insert the given value into the tree
#     def insert(self, value):
#         self.value = value
#         node = self.value
#         #if inserting we must have a tree/root
#         if self.queue.size == 0:
#             self.queue.enqueue(node)
#             self.queue.size+=1
#             print("queue was empty")
#             print(self.queue.size, "size of queue")
#         # what is the root?
#         else:
#             root = self.queue.storage.head
#             root_value = root.value
#             if node >= root_value:
#                 print(f"node {node} is >= root_value {root_value}")
#                 # node.right = True
#                 self.queue.enqueue(node)
#             elif node < root_value:
#                 print(f"node {node} is < root_value {root_value}")
#                 # node.left = True
#                 self.queue.enqueue(node)
#         #if value is less than (the root) self.value go left, make a new tree(node) if empty
#         #else keep going (recursion)
#             else:
#                 self.insert(value)
#         #if greater than or equal to then go right, make another tree node if empty, otherwise
#         #keep going
#         pass

   