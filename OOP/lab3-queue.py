class QueueError(IndexError):
    pass


class Queue:
    def __init__(self):
        self._queue = []
    def put(self , element):
        self._queue.insert(0 , element)
    def get(self):
        if self._queue:
            ele = self._queue[-1]
            self._queue.pop()
            return ele
        else:
            raise QueueError

class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
    
    def isempty(self):
        return not self._queue
        

que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
