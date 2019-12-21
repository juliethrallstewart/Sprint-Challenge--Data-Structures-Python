class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  def reverse_list(self):
       prev_node = None
       current_node = self.head
       next_node = None
       while current_node:
             next_node = current_node.next_node
             current_node.next_node = prev_node #initially set to none to create end of list
             prev_node = current_node
             current_node = next_node
       self.head = prev_node  
          
  def get_list(self):
        print(self.head.value)
        print(self.head.get_next().value)
        print(self.head.get_next().get_next().value)
        print(self.head.get_next().get_next().get_next().value)
  
   
        

l = LinkedList()
l.add_to_head(1)  
l.add_to_head(2)
l.add_to_head(3)
l.add_to_head(4)
print(l.reverse_list())
# l.get_list()


#alt
# def reverse_list(self):
#   p_node = None
#        c_node = self.head
#        n_node = None
#        while c_node:
#              n_node, c_node.next_node = c_node.next_node, p_node
#              p_node, c_node = c_node, n_node
            
#        self.head = p_node 