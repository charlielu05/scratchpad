from linked_list import LinkedList, Node

class SuperList(LinkedList):

    def print_all(self):
        current_node = self.first_node

        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def print_last(self):
        current_node = self.first_node

        while current_node.next is not None:
            current_node = current_node.next

        print(current_node.data)

    def reverse(self):
        current_node = self.first_node
        previous_node = None

        while current_node.next is not None:
            next_node = current_node.next
            current_node.next = previous_node

            previous_node = current_node
            current_node = next_node

        self.first_node = previous_node

if __name__ == "__main__":

# print all elements of linked list
    node_1 = Node("a")
    node_2 = Node("b")
    node_3 = Node("c")
    node_1.next = node_2
    node_2.next = node_3

    super_list = SuperList(node_1)
    super_list.print_all()

# print last element of linked list
# if the next node is none, we know its the last node
    super_list.print_last()

# reverse list
    super_list.reverse()
    super_list.print_all()


