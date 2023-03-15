class Heap:
    def __init__(self):
        self.data = []
    
    def root_node(self):
        return self.data[0]
    
    def last_node(self):
        return self.data[-1]

    @staticmethod
    def left_child_index(index):
        return (index * 2) + 1

    @staticmethod
    def right_child_index(index):
        return (index * 2) + 2
    
    @staticmethod
    def parent_index(index):
        return int((index-1) / 2)

    def has_greater_child(self, index)->bool:
        # check whether the node at index has left or right child and if either of those child
        # are greater than the node at index
        return (
                (self.data[self.left_child_index(index)] > self.data[index] and self.data[self.left_child_index(index)] is not None) 
                or
                (self.data[self.right_child_index(index)] > self.data[index] and self.data[self.right_child_index(index)] is not None)
                )

    def calculate_larger_child_index(self, index):
        # if there is no right child, we simply return left
        if self.data[self.right_child_index(index)] is None:
            return self.left_child_index(index)
        
        # if right child is greater than left child node
        elif self.data[self.right_child_index(index)] > self.data[self.left_child_index(index)]:
            return self.right_child_index(index)
        
        # if left child is equal or greater than right child node
        else:
            return self.left_child_index(index)

    def delete(self):
        # we only delete the root node, so we pop the last node from array and make it the root node
        self.data[0] = self.data.pop()

        # track index of the "trickle node"
        trickle_node_idx = 0

        # perform trickle down while there is a greater child node
        while (self.right_child_index(trickle_node_idx) <= len(self.data) or self.left_child_index(trickle_node_idx) <= len(self.data)) and self.has_greater_child(trickle_node_idx):
            # swap with larger child
            larger_child_index = self.calculate_larger_child_index(trickle_node_idx)

            # swap
            self.data[trickle_node_idx], self.data[larger_child_index] = self.data[larger_child_index], self.data[trickle_node_idx]

            # update the trickle node
            trickle_node_idx = larger_child_index

    def insert(self, value:int):
        self.data.append(value)

        new_node_idx = len(self.data) - 1

        # trickle up algorithm
        # if the new node is not in the root position and its greater than its parents node
        while new_node_idx > 0 and self.data[new_node_idx] > self.data[self.parent_index(new_node_idx)]:
            # swap the new node with the parent node
            self.data[new_node_idx], self.data[self.parent_index(new_node_idx)] = self.data[self.parent_index(new_node_idx)], self.data[new_node_idx]
            # updat the index of the new node
            new_node_idx = self.parent_index(new_node_idx)

if __name__ == "__main__": 
    test_heap = Heap()
    test_heap.data = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]

    print(test_heap.root_node())
    print(test_heap.last_node())

    left_idx = test_heap.left_child_index(3) 

    assert test_heap.data[left_idx] == 86
    print(len(test_heap.data))

    # insert
    test_heap.insert(30)
    print(len(test_heap.data))

    assert test_heap.data[2] == 30

    # test has greater child
    assert test_heap.has_greater_child(0) == False
    test_heap.data[0] = 1
    assert test_heap.has_greater_child(0) == True

    # test calculate larger child index
    assert test_heap.calculate_larger_child_index(0) == 1

    # test delete
    test_heap = Heap()
    test_heap.data = [100, 88, 25, 87, 16, 8, 12, 86, 50, 2, 15, 3]
    test_heap.delete()
    assert test_heap.root_node() == 88