from doubly_linked_list import DoublyLinkedList


# class RingBuffer:
#     def __init__(self, capacity):
#         self.capacity = capacity
#         self.current = None
#         self.storage = DoublyLinkedList()
    
#     def __repr__(self):
#         return f"""Capacity: {self.capacity}
#         Current = {self.current}
#         Storage = {self.storage}
#         """
      

#     def append(self, item):
#         if self.storage.length == self.capacity:
#             self.current.value = item

#             if self.current is self.storage.tail:
#                 self.current = self.storage.head
#             else:
#                 self.current = self.current.next

#         elif self.storage.length < self.capacity:
#             self.storage.add_to_tail(item)
#             self.current = self.storage.head

               
 
#     def get(self):
#         # Note:  This is the only [] allowed
#         list_buffer_contents = []
#         current = self.storage.head
#         print(f"show storage length:{self.storage.length}")
#         if current == None:
#             print(f"current is None")
#         while current is not None:
#             list_buffer_contents.append(current.value)
#             current = current.next

#         # TODO: Your code here

#         # list_buffer_contents.sort()
#         print(f"length of buffer contents: {len(list_buffer_contents)}")
#         return list_buffer_contents

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
    def append(self, item):
        if len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail
        elif self.current == self.storage.tail:
            self.storage.remove_from_head()
            self.storage.add_to_head(item)
            self.current = self.storage.head
        else:
            self.current.insert_after(item)
            self.storage.length += 1
            self.current = self.current.next
            self.storage.delete(self.current.next)
    def get(self):
        list_buffer_contents = list()
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next
        return list_buffer_contents

buffer_2 = RingBuffer(5)
for i in range(23):
    print(i)
    buffer_2.append(i)

print(buffer_2.get())
# ----------------Stretch Goal-------------------
# r = RingBuffer(5)
# r.append(1)
# r.append(2)
# r.append(3)
# r.append(4)
# r.append(5)
# r.append(6)
# print(r.get())

# r.append('a')
# r.append('b')
# r.append('c')
# r.append('d')
# r.append('e')
# r.append('f')
# r.append('g')
# r.append('h')
# r.append('i')
# r.append('j')
# r.append('k')

# print(r.get())

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass



        # def append(self, item):
        #     if len(self.storage) < self.capacity:
        #     self.storage.add_to_tail(item)
        #     self.current = self.storage.tail
        
        # elif self.current == self.storage.tail:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        #     self.current == self.storage.head
        # else: 
        #     self.current.insert_after(item)
        #     self.storage.length += 1
        #     self.current = self.current.next
        #     self.storage.delete(self.current.next)