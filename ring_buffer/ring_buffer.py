from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 0
        self.storage = DoublyLinkedList()
        self.dict = dict()

    def append(self, item):

        
       
        # if self.current > self.capacity:
        #     self.storage.remove_from_head()
        #     self.storage.add_to_head(item)
        # else:
        #     self.storage.add_to_tail(item)
        #     self.current += 1
        # if item in self.dict:
        #     node = self.dict[item]
        #     node.value = (item,item)
        #     self.storage.move_to_front(node)

        # the oldest element in the ring buffer is overwritten by the newest
        if self.current == self.capacity:
            del self.dict[self.storage.head.value[0]] # remove from dict
            self.storage.remove_from_head() #remove from head
            self.current -=1

        self.storage.add_to_tail((item,item))
        self.dict[item] = self.storage.tail
        self.current += 1

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value[1])
            current = current.next

        # TODO: Your code here

        
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
# r.append('f') #['f', 'b', 'c', 'd', 'e'])

r.append('f')



print(r.get())
# r.append('g')
# r.append('h')
# r.append('i')

print(r.get()) #['f', 'g', 'h', 'i', 'e'])

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
