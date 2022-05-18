class Node():

    def __init__(self,number):
        self.data=number
        self.next=None


class Linkedlist():
    def __init__(self):
        self.head=None


    def append(self, value):
        if self.head is None:
            self.head=Node(value)

        else:
            current_node=self.head
            while current_node.next is not None:
                current_node=current_node.next
                current_node.next=Node(value)

    def Showele(self):
        current=self.head

        while current is not None:
            print(current.data)
            current=current.next

    def length(self):
        current=self.head
        r=0
        while current is not None:
            r+=1
            current=current.next
            return r

    def location(self,position):
        current=self.head
        i=0
        while current is not None:
            if i==position:
                current=current.next
                return None



l=Linkedlist()
#l.head=Node(2)
#l.head.next=Node(3)
#l.head.next.next=Node(4)
l.append(2)
l.append(3)
l.append(4)
#print(l.head.data,l.head.next)
l.Showele()
l.length()
l.location(2)
#print(l.head.data,l.head.next.data,l.head.next.next)
#c=Node(2)
#c.data
#print(c.data)

#c=Node()
#c.data
#print(c.data)
#c.data=10
#print(c.data)




