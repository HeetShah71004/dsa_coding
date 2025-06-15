class MyQueue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x):
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        if self.empty():
            return None
        return self.s1.pop()

    def peek(self):
        if self.empty():
            return None
        return self.s1[-1]

    def empty(self):
        return len(self.s1) == 0


# 📥 Example Input and 📤 Output
if __name__ == "__main__":
    q = MyQueue()
    
    print("Pushing: 10, 20, 30")
    q.push(10)
    q.push(20)
    q.push(30)

    print("Peek:", q.peek())     # Output: 10
    print("Pop:", q.pop())       # Output: 10
    print("Peek:", q.peek())     # Output: 20
    print("Empty:", q.empty())   # Output: False
    q.pop()
    q.pop()
    print("Empty after popping all:", q.empty())  # Output: True