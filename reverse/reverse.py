class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        current_node = node

        # the loop will run til the next_node reaches the tail (None)
        while current_node:
            # I want to set the next_node to  a variable 
            next_node = current_node.next_node
            #now i will do the reversing. This will bring the current node to the head
            current_node.next_node = prev
            #Set previous to a variable so it can be used the next time through
            # 1st node 1st time thru, 2nd node 2nd time thru, it'll repeat like this
            prev = current_node
            #now I'll update the current_node so the loop will run or exist if none
            current_node = next_node

        #update the head to be the last previous variable before the loop exits
        self.head = prev

