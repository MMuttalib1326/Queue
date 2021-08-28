# Implementation of queue
# python language

class queue:
    def __init__(self):
        self.item=[]
    def __str__(self):
        value=[str(x) for x in self.item]
        value=' '.join(value)

# is empty
    def isempty(self):
        if self.item==[]:
            return True
        else:
            return False

# enqueue
    def enqueue(self,value):
        self.item.append(value)
        return "The element is inserted at the end of queue"

# dequeue
    def dequeue(self):
        if self.isempty():
            return "There is not any element in the queue"
        else:
            return self.item.pop(0)

# peek
    def peek(self):
        if self.isempty:
            return "There is no element in the queue"
        else:
            return self.item[0]

# delete
    def delete(self):
        self.item=None

customqueue=queue()
customqueue.enqueue(1)
customqueue.enqueue(2) 
customqueue.enqueue(3)
print(customqueue.enqueue())
#print(customqueue)                                                                

