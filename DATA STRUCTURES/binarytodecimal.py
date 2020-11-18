class node:
    def __init__(self, data =None):
        self.data = data
        self.next = None

#We will be creating now a linked list class
#which will be basically a wrapper that will wrap
#above notes

class linked_list:
    def __init__(self):
        self.head = node()

    def append(self,data):
        new_node = node(data)
        cur= self.head
        while cur.next!= None:
            cur= cur.next
        cur.next= new_node


    def getDecimalValue(self):
        result = ""
        cur= self.head
        while cur.next!=None:
            cur=cur.next
            result+=str(cur.data)
        
        print(int(result, 2))



my_list= linked_list()
my_list.append(1)
my_list.append(0)
my_list.append(1)

my_list.getDecimalValue()

    
