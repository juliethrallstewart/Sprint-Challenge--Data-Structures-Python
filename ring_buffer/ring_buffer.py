from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = 1
        self.storage = DoublyLinkedList()

    def append(self, item):
        print(f"{self.current}, {self.capacity}")
        if self.current > self.capacity:
            self.storage.remove_from_tail()
            self.storage.add_to_head(item)
        else:
            self.storage.add_to_head(item)
            self.current += 1
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
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
r.append('f')
r.append('g')
r.append('h')
r.append('i')

print(r.get())

class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
