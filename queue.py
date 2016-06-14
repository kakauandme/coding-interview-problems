class Queue(object):

    def __init__(self):
        """Return a Customer object whose name is *name*.""" 
        self.items = []
    def __str__(self):
        return " ".join([str(s) for s in self.items])
      
    def add(self, data):
        self.items.append(data)
    def peak(self):
        return self.items[-1]
    def pop(self):
        return self.items.pop()
    def output(self):
        print(str(self.data) + " ", end="" )
        tmp = self
        while tmp.next:
            tmp = tmp.next
            print(str(tmp.data) + " ", end="" )


a = Queue()
a.add(1)
a.add(2)
a.add(3)

print(a.peak())
print(a.pop())
print(a)
a.add(4)
print(a)
