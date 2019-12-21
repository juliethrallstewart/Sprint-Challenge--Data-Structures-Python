from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
      

    def append(self, item):

        # if len(self.storage) != self.capacity:
        #     print(f"storage 1: {self.storage.length}, capacity: {self.capacity}")

        #     self.storage.add_to_tail(item)
        #     return
     
        if len(self.storage) == self.capacity:
            print(f"storage 2: {self.storage.length}, capacity: {self.capacity}")
            # self.current = self.storage.head
            
            print(f"self.current is not None: {self.current.value}, inserting {item}")
            current_node = self.current
            print(f"current node line 25: {current_node.value}")
            print(f"size of storage before insert: {len(self.storage)}")

            current_node.insert_after(item)
          
            print(self.storage.get_items())
            self.storage.length += 1
            print(f"size of storage after insert: {len(self.storage)}")

            print(f"inserted {item} after current_node {current_node.value}")
            new_node = current_node.next
            # print(f"now {new_node.value} is the new_node")
            self.current = new_node.next
            print(f"now {self.current.value} is the new_node")
            self.storage.delete(current_node)
            print(f"size of storage after delete: {len(self.storage)}")
            if self.current == None:
                self.current = self.storage.head
                return
            else:
                
                return

        if len(self.storage) != self.capacity:
                print(f"storage 1: {self.storage.length}, capacity: {self.capacity}")

                self.storage.add_to_tail(item)
                self.current = self.storage.head
                return
            
 
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        # TODO: Your code here

        # list_buffer_contents.sort()
        return list_buffer_contents

# ----------------Stretch Goal-------------------
r = RingBuffer(5)
# r.append(1)
# r.append(2)
# r.append(3)
# r.append(4)
# r.append(5)
# r.append(6)
# print(r.get())

r.append('a')
r.append('b')
r.append('c')
r.append('d')
r.append('e')
# # r.append('f') #['f', 'b', 'c', 'd', 'e'])

r.append('f')



# print(r.get())
r.append('g')
r.append('h')
r.append('i')
# r.append('j')
# r.append('k')

print(r.get()) #['f', 'g', 'h', 'i', 'e'])

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass


#  print(f"storage length: {self.storage.length}, capacity: {self.capacity}")
#             if self.current is None:
#                 print(f"self.current {self.current} == none")
#                 self.storage.remove_from_head()
#                 self.storage.add_to_head(item)
#                 self.current = self.storage.head
#             else:
#                 self.storage.head.insert_after(item) #insert new item 
#                 self.storage.head.next.next.delete()
#                 self.storage.add_to_tail(self.storage.head.value)
#                 self.storage.remove_from_head()
#                 print(self.storage.length)
#                 # self.storage.head = self.current.next
#               # set the new head to the next value
      
#                 # self.append(item)
                
     
             
#         else:
#             print(f"storage length: {self.storage.length}")
#             self.storage.add_to_tail(item)