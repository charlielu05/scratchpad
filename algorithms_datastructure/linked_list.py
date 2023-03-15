
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self, node):
        self.first_node = node

    def read(self, idx):
        current = self.first_node
        current_idx = 0

        while current_idx < idx:
            current = current.next
            current_idx += 1

        return current.data

    def search(self, value):
        current = self.first_node
        current_idx = 0

        while current.data != value:
            current = current.next
            current_idx += 1
        
        return current_idx

    def insertion(self, idx, value):
        new_node = Node(value)

        if idx == 0:
            new_node.next = self.first_node
            self.first_node = new_node

            return

        current_idx = 0
        current_node = self.first_node

        while current_idx < idx -1:
            current_node = current_node.next
            current_idx += 1
        
        new_node.next = current_node.next
        current_node.next = new_node
    
    def delete(self, idx):
        if idx == 0:
            self.first_node = self.first_node.next

            return
        
        current_idx = 0
        current_node = self.first_node

        while current_idx < idx - 1:
            current_node = current_node.next
            current_idx += 1
        
        node_after_deletion = current_node.next.next
        current_node.next = node_after_deletion

if __name__ == "__main__":
    test = Node("a")
    test2 = Node("b")
    test3 = Node("c")
    test.next = test2
    test2.next = test3

    print(test.next)

    linked_list = LinkedList(test)

    print(linked_list.first_node.next)

    print(linked_list.read(1))

    print(linked_list.search("c"))

    # test insertion
    linked_list.insertion(0, "d")
    print(linked_list.first_node)

    # test insertion
    linked_list.insertion(2, "f")
    print(linked_list.read(2))

    # test deletion
    linked_list.delete(2)
    print(linked_list.read(2))