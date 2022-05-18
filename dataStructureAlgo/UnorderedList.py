class Node():
    def __init__(self,data=None,next_node=None):
        self.data=data
        self.next_node=next_node

    def get_data(self):
        return self.data



    def get_next(self):
        return self.next_node

    def set_next(self,new_next):
        self.next_node=new_next


class Linkedlist():
    def __init__(self,head=None):
        self.head=head

    def display(self):
        current=self.head

        while current:
            print(current.data,end='')
            current=current.next_node


    def End(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node

        else:
            current=self.head
            while current.next_node is not None:
                current=current.next_node
                current.next_node=new_node


    def file(self):
        current=self.head
        temp=" "
        while current is not None:
            temp=temp+current.data+" "
            current=current.next_node

        return temp

    def Search(self,data):
        current=self.head
        found=False
        while current and found is False:
            if current.get_data()==data:
                found=True

            else:
                current=current.get_next()

    def delete(self,data):
        current=self.head
        previous=None
        found=False

        while current and found is not None:
            if current.get_data==data:
                found=True

            else:
                previous=current.get_next()

            if current is None:
                print("data not found")

            else:
                previous.get_next(current.get_next())



if __name__=="__main__":
    llist=Linkedlist()

    with open("D:/GameCopyRight.txt", "r") as f:



        for line in f:
            words = line.split()
            for word in words:
                llist.End(word)
    print("\n File contents in the List is:")
    llist.display()

    # Searching the word in the Linked List
    Searchword = input("\nEnter the word to be searched : ")
    if (llist.Search(Searchword)):
        llist.delete(Searchword)
        print("Word", Searchword, " found in the Linked List and deleted")
    else:
        print("Word", Searchword, " not found in the Linked List")
    # llist.displayall()

    # Updated Linked list is stored in the file a_file.txt










