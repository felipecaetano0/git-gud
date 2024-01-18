
class DataStructure:
    def __init__(self, x: list = None):
        self.data = x if x else []

    def insert(self, value):
        ...

    def get(self):
        ...


class Queue(DataStructure):
    def insert(self, value):
        self.data.append(value)

    def get(self):
        return self.data.pop(0)


class Stack(DataStructure):

    def insert(self, value):
        self.data.append(value)

    def get(self):
        return self.data.pop()


if __name__ == "__main__":
    q = DataStructure()

    q.insert(1)
    q.insert(2)
    q.insert(3)

    print(q.get())
    print(q.get())
    print(q.get())
