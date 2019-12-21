from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
      

    def append(self, item):
        if len(self.storage) == self.capacity:
            current_node = self.current
            if current_node:
                current_node.insert_after(item)
                self.storage.length += 1
                new_node = current_node.next
                self.current = new_node.next
                self.storage.delete(current_node)

                if self.current == None:
                    self.current = self.storage.head
                    return
         
        if len(self.storage) != self.capacity:
                self.storage.add_to_tail(item)
                self.current = self.storage.head
                return
            
 
    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []
        current = self.storage.head
        print(f"show storage length:{self.storage.length}")
        while current:
            print(f"while current {current.value}")
            list_buffer_contents.append(current.value)
            current = current.next

        # TODO: Your code here

        # list_buffer_contents.sort()
        print(f"length of buffer contents: {len(list_buffer_contents)}")
        return list_buffer_contents

buffer_2 = RingBuffer(5)
for i in range(22):
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

