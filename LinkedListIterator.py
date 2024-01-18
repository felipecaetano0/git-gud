
class LinkedListNode:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class LinkedListIterator:
    def __init__(self, from_list=None):
        self.start_node = None
        self.last_node = None
        if from_list:
            for element in from_list:
                self.append(element)

    def append(self, value):
        if not self.start_node:
            self.last_node = self.start_node = LinkedListNode(value)
        else:
            self.last_node.next_node = LinkedListNode(value)
            self.last_node = self.last_node.next_node

    def get(self, index):
        current_node = self.start_node
        iterations_counter = 0
        while iterations_counter < index:
            iterations_counter += 1
            current_node = current_node.next_node
        return current_node

    def remove(self, index):
        previous_node = self.get(index - 1)
        previous_node.next_node = previous_node.next_node.next_node

    def insert(self, index, value):
        previous_node = self.get(index - 1)
        new_node = LinkedListNode(value, previous_node.next_node)
        previous_node.next_node = new_node

    def __iter__(self):
        self.iteration_pointer = self.start_node
        return self

    def __next__(self):
        if self.iteration_pointer is None:
            raise StopIteration
        else:
            return_value = self.iteration_pointer
            self.iteration_pointer = self.iteration_pointer.next_node
            return return_value

    def __str__(self):
        # FIXME :: Chuck Norris completely disapproved the following code and rewrote it properly
        # s = "{"
        # current_node = self.start_node
        # while current_node:
        #     s += f'{current_node.value}'
        #     current_node = current_node.next_node
        #     if current_node:
        #         s += ', '
        # s += '}'
        # return s
        s = "{"
        for self_iterator in self:
            s += str(self_iterator.value)
            if self_iterator.next_node:
                s += ', '
        s += '}'
        return s


if __name__ == "__main__":
    myIter = LinkedListIterator([1, 1, 2, 3.14, "foo"])
    myIter.append("bar")
    print(myIter)

    myIter.remove(4)
    print(myIter)

    myIter.insert(4, 'git gud')
    print(myIter)
