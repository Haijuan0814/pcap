class QueueError(Exception):  # Choose base class for the new exception.
    pass
    



class Queue:
    def __init__(self):
        self.queue = []
    
    def put(self, element):
        self.queue.insert(0, element)

    def get(self):
        if not self.queue:
            raise QueueError("Queue error")
        return self.queue.pop()

       

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
