# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 17:55:26 2017

@author: Trenton
"""

class Stack():
    """ Python list stack in LIFO format """
    
    def __init__(self, capacity=None):
        self._data = []
        self._capacity = capacity
    
    def __len__(self):
        return len(self._data)
    
    def push(self, item):
        if self._capacity and len(self._data) >= self._capacity:
            raise IndexError('Stack is full')
        self._data.append(item)
            
    def pop(self):
        if self.isEmpty():
             raise IndexError('Stack is empty')
        return self._data.pop()
    
    def peek(self):
        if self.isEmpty():
             raise IndexError('Stack is empty')
        return self._data[-1]
    
    def isEmpty(self):
        return (len(self._data)==0)
    
    def __str__(self):
        return str(self._data)
 
#push: O(1), pop: O(1), peek: O(1), isEmpty: O(1)    
#space: O(n), where n is the numbers of items in the stack
    
#test    
MyStack = Stack()
MyStack.push(5)
MyStack.push(8)
MyStack.push(1)
MyStack.push(11)
MyStack.push(4)
print('The top of the stack is ' + str(MyStack.peek()))
print('The stack currently looks like this: ' + str(MyStack))
MyStack.pop()
print('The stack now looks like this: ' + str(MyStack))

