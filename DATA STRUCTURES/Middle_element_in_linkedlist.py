class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


#We will be creating now a linked list class
#which will be basically a wrapper that will
#wrap above notes


class linked_list:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next!=None:
            cur= cur.next
        cur.next = new_node


    def middle_element(self):
        slow_pointer = self.head
        fast_pointer = self.head

        if self.head is not None:
            while(fast_pointer is not None and fast_pointer.next is not None):
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next

            print(slow_pointer.data)



my_list = linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.append(5)
my_list.middle_element()













