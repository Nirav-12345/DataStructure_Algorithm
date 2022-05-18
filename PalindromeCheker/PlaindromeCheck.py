class Stack():
    def __init__(self):
        self.values=[]

    def push(self,value):
        self.values.append(value)

    def pop(self):
        self.values.pop()


class Queue():
    def __init__(self):
        self.values=[]

    def push(self, value):
        self.values.append(value)

    def pop(self):
        self.values.pop()

stack=Stack()
queue=Queue()

class PalindromeChexker():



    def __init__(self, word):
        self.word = word
        self.stack = Stack()
        self.queue = Queue()

    def Palindrome(self):

        for letter in self.word:
            self.queue.push(letter)
            self.stack.push(letter)

        for i in range(len(self.word)):
            if self.queue.pop() != self.stack.pop():
                return False

        return True


if __name__=="__main__":
    s = str(input())
    r=PalindromeChexker(s)

    if r.Palindrome():
        print(s,"Palindrome")

    else:
        print(s,"not a palindrome")
