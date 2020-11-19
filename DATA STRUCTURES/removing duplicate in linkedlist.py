class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head = node()


    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def display(self):
        elems=[]
        cur = self.head
        while cur.next is not None:
             cur= cur.next
             elems.append(cur.data)
             
        print(elems)

    def removeduplicate(self):
        cur = self.head

        while cur.next is not None:
            if cur.data == cur.next.data:
                cur.next= cur.next.next
            else:
                cur= cur.next

        cur = self.head
        return cur
    



mylist = linked_list()
mylist.append(1)
mylist.append(2)
mylist.append(2)
mylist.display()
mylist.removeduplicate()
mylist.display()
           
