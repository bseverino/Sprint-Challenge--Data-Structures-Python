from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def replace(self, item):
        current_node = self.storage.head
        while current_node != self.current:
            current_node = current_node.next
        current_node.value = item
        if current_node.next:
            self.current = current_node.next
        else:
            self.current = self.storage.head

    def append(self, item):
        if len(self.storage) == 0:
            self.storage.add_to_head(item)
            self.current = self.storage.head
        elif len(self.storage) < self.capacity:
            self.storage.add_to_tail(item)
        else:
            self.replace(item)
        

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        current_node = self.storage.head

        if current_node.value:
            list_buffer_contents.append(current_node.value)
        
        while current_node.next:
            current_node = current_node.next
            if current_node.value:
                list_buffer_contents.append(current_node.value)


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None for i in range(0, capacity)]
        self.current = 0

    def append(self, item):
        self.storage[self.current] = item
        if self.current == self.capacity - 1:
            self.current = 0
        else:
            self.current += 1

    def get(self):
        return [i for i in self.storage if i]