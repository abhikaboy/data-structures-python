class Node:
    def __init__(self, value, nextNode = None):
        self.value = value
        self.next = nextNode
    def get_next(self):
        return self.next
    def set_next(self, nextNode):
        self.next = nextNode
    def get_value(self):
        return self.value

#
#
class LinkedList:
    def __init__(self, head = None):
        self.head = head    
    def insert(self, value):
        currentNode = self.head
        previousNode = self.head
        while currentNode:
            previousNode = currentNode
            currentNode = currentNode.get_next()
        # reached the end of the list 
        previousNode.set_next(Node(value))
    def stringify(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.get_value())
            currentNode = currentNode.get_next()
        print("-------------------")
    def remove(self, value):
        currentNode = self.head;
        previousNode = self.head;
        while currentNode:
            if currentNode.get_value() is value:
                previousNode.set_next(currentNode.get_next())
                break
            previousNode = currentNode
            currentNode = currentNode.get_next()
        return self
    def swap(self, value1, value2):
        return self
    def reverse(self):
        return self
    def insertOrderly(self, value1):
        return self
    def nth_last_node(self, n):
        return self
    def middle(self):
        return self

# Testing 
testList = LinkedList(Node(1))
testList.stringify()

testList.insert(2)
testList.insert(3)
testList.insert(4)
testList.insert(5)
testList.stringify()

testList.remove(3)
testList.stringify()

"""
Algorithmic tips: 
If you ever need to keep track of multiple positions 
or you feel like you need to create another data type to solve a problem (List)

CONSIDER USING MULTIPLE POINTERS! 
Pointers can move in parallel or differing speeds

"""