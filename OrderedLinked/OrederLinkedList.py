class Node():
    def __init__(self,data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, value):
        #  Create  node
        node = Node(value)
        if (self.head == None):
            self.head = node
        else:
            temp = self.head
            #  Find last node
            while (temp.next != None):
                #  Visit to next node
                temp = temp.next

            #  Add node at last position
            temp.next = node



    def display(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
        return temp


    def arrange(self,element):
        if (self.head == None):
            self.head = element
        elif (self.head.data >= element.data):
            element.next = self.head
            self.head = element
        else:
            temp = self.head
            #  Finding location of inserting nodes
            while (temp.next != None and
                   temp.next.data < element.data):
                #  Visit to next node
                temp = temp.next

            element.next = temp.next
            temp.next = element


    def sort(self):
        if (self.head == None):
            return

        temp = self.head
        hold = None
        self.head = None
        #  iterate linked list nodes and add in sorted order
        while (temp != None):
            hold = temp
            #  Visit to next node
            temp = temp.next
            hold.next = None
            #  Logic to add node
            self.arrange(hold)

    def Index(self, position):
        temp = self.head
        if self.head:
            while temp.next:
                if temp== position:
                    return temp



                else:
                    return -1

    def search(self,data):
        temp=self.head
        found=False

        while temp and found is False:
            if temp==data:
                found=True
                return

            else:
                temp=temp.next




sll=LinkedList()
sll.insert(3)
sll.insert(4)
sll.insert(5)
sll.insert(1)
sll.insert(6)
sll.insert(4)
print(sll.Index(5))
sll.sort()
sll.search(6)
sll.display()
