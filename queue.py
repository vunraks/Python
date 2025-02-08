from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.popleft()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def reverse(self):
        self.items = deque(reversed(self.items))
    
    def copy(self):
        new_queue = Queue()
        new_queue.items = self.items.copy()
        return new_queue

class LimitedQueue(Queue):
    def __init__(self, max_size):
        super().__init__()
        self.max_size = max_size
    
    def enqueue(self, item):
        if self.size() >= self.max_size:
            print("Очередь заполнена")
        else:
            super().enqueue(item)




if __name__ == "__main__":
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    print("Оригинальная очередь:", list(q.items))
    
    q.reverse()
    print("Перевернутая очередь:", list(q.items))
    
    q_copy = q.copy()
    print("Копия очереди:", list(q_copy.items))
    
    lq = LimitedQueue(2)
    lq.enqueue(10)
    lq.enqueue(20)
    lq.enqueue(9)
    print("Ограниченная очередь:", list(lq.items))
