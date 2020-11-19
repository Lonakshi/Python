#Reversing a linkedlist

class node:
    def __init__(self, data= None):
        self.data = data
        self.next = None

class linked_list:
    def __init__(self):
        self.head= None


    def append(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node
     


    def reverse(self):
         if self.head is None or self.head.next is None:
            return
         
         prev= None
         cur = self.head
         while cur is not None:
             temp = cur.next
             cur.next =prev
             prev = cur
             cur = temp
         self.head = prev
            
         

  
            

        
         


         


    def display(self):
         elems = []
         cur_node = self.head
         while cur_node is not None:
             
             elems.append(cur_node.data)
             cur_node = cur_node.next
             

         print(elems)



my_list= linked_list()
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
my_list.reverse()
my_list.display()
      





        
        

    
