class Node(object):

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def __str__(self):
        return str(self.data)

    
    def get_next(self):
        return self.next_node

   



class LinkedList(object):

    def __init__(self, head=None):
        self.head = head

    def __str__(self):
       
        tmp = self.head
        res = str(tmp)
        while tmp.get_next():
            tmp = tmp.get_next()
            res+=" " + str(tmp)
        return res

    def add(self, data):
        tmp = Node(data, self.head)
        self.head = tmp

l = LinkedList(Node(1))
l.add(2)
l.add(2)
l.add(2)
print(l)