
class EmptyListException(Exception):                                                                                              
    def __init__(self, message):                                                                                                  
        self.message = message                                                                                                    
        super().__init__(message)   

class Node:
    def __init__(self, value):
        self._value = value
        self._next = None
    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=None):
        self._head = None
        self._len = 0
        if values is not None:
            for value in values:
                self.push(value)

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current._value 
            current = current._next

    def __len__(self):
        return self._len

    def head(self):                                                                                                                   
        if self._head is None:                                                                                                        
            raise EmptyListException("The list is empty.")                                                                            
        return self._head     

    def push(self, value):
        new_node = Node(value)
        new_node._next = self._head
        self._head = new_node
        self._len += 1
    def pop(self):
        if self._head is None:
            raise EmptyListException("The list is empty.")
        value = self._head._value 
        self._head = self._head._next
        self._len -= 1
        return value

    def reversed(self):
        return LinkedList(list(self))
