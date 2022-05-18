class Queue():
    def __init__(self):
        self.balance=0

    def enqueue_Cash(self):
        amount=int(input("Enter Amount"))
        self.balance +=amount
        print(amount)

    def dequeue_cash(self):
        amount=int(input("For withdraw"))
        if self.balance >=amount:
            self.balance -=amount
            print(amount)
        else:
            print("Insuffeciant Balance")

    def display_cash(self):
        print(self.balance)


if __name__=="__main__":
    q=Queue()
    try:

        v=int(input("Enter number"))

        if v==1:
            q.enqueue_Cash()

        elif v==2:
            q.dequeue_cash()

        elif v==3:
            q.display_cash()


        else:
            print("Please give proper output")

    except:
        print("nothing found")


