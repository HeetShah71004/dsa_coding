from queue import Queue

class MyStack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x):  # O(n)
        while not self.q1.empty():
            self.q2.put(self.q1.get())
        self.q1.put(x)
        while not self.q2.empty():
            self.q1.put(self.q2.get())

    def pop(self):
        if self.q1.empty():
            return None
        return self.q1.get()

    def top(self):
        if self.q1.empty():
            return None
        front = self.q1.get()
        self.q1.put(front)
        for _ in range(self.q1.qsize() - 1):
            self.q1.put(self.q1.get())
        return front

    def empty(self):
        return self.q1.empty()


# 📥 Example Input and 📤 Output
if __name__ == "__main__":
    stack = MyStack()
    
    print("Pushing: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top:", stack.top())    # Output: 30
    print("Pop:", stack.pop())    # Output: 30
    print("Top:", stack.top())    # Output: 20
    print("Empty:", stack.empty()) # Output: False
    stack.pop()
    stack.pop()
    print("Empty after popping all:", stack.empty())  # Output: True
