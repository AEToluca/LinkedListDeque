class _Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Deque:
    def __init__ (self):
        self.size = 0
        self.front_head = None
        self.back_head = None

    def insertFront(self, value: int):
        newNode = _Node (value) #Create new node
        newNode.next = self.front_head #Make old head next for new node
        self.front_head = newNode #Make old head new node
        self.size += 1 #Increment size

        #Do same as add front but use back node
    def insertBack(self, value: int):
        newNode = _Node(value)
        newNode.next = self.back_head
        self.back_head = newNode
        self.size += 1
    
    def removeFront(self) -> int:
        if self.front_head is None:
            if self.back_head is None:
                raise IndexError("Deque is empty")
            self.reverse_back_to_front()
        done = self.front_head.value
        self.front_head = self.front_head.next
        self.size -= 1
        return done
    
        #same as front but use back node
    def removeBack(self) -> int:
        if self.back_head is None:
            if self.front_head is None:
                raise IndexError("Deque is empty")
            self.reverse_front_to_back()
        done = self.back_head.value
        self.back_head = self.back_head.next
        self.size -= 1
        return done

    def isEmpty(self) -> bool: #Check if deque is empty
        return self.front_head is None and self.back_head is None
    
    def getSize(self) -> int:
        return self.size
    
    def reverseBackToFront(self): #Helper method to reverse list in case of one list empty.
        while self.back_head:
            node = self.back_head
            self.back_head = self.back_head.next
            node.next = self.front_head
            self.front_head = node

    def reverse_front_to_back(self): #Helper method to reverse list in case of one list empty.
        while self.front_head:
            node = self.front_head
            self.front_head = self.front_head.next
            node.next = self.back_head
            self.back_head = node
            
def main():
    dq = Deque()
    dq.insertFront(10)
    dq.insertBack(20)
    dq.insertFront(5)
    print(dq.removeFront()) # Output: 5
    print(dq.removeBack()) # Output: 20
    print(dq.isEmpty()) # Output: False
    print(dq.removeFront()) # Output: 10
    print(dq.isEmpty()) # Output: True

if __name__ == "__main__":
    main()
    
        


    

