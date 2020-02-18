class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head
    
    def insert_recur(self, item, position):
        pass
    
    def insert(self, item, position):
        N = Node(item)
        if not self.head:
            self.head = N
        else:
            if position == 0:
                N.next = self.head
                self.head = N
            else:
                temp = self.head
                count = 1
                while count != position:
                    if not temp.next:
                        raise IndexError('List index out of range!')
                    temp = temp.next
                    count += 1
                N.next = temp.next
                temp.next = N
    
    def append(self, item):
        N = Node(item)
        if not self.head:
            self.head = N
        else:
            temp = self.head
            while True:
                if temp.next:
                    temp = temp.next
                else:
                    temp.next = N
                    break
        
    def delete(self, item):
        if not self.head:
            raise Exception('List is empty!')
        else:
            temp = self.head
            if self.head.value == item:
                self.head = self.head.next
                del temp
            else:
                while True:
                    if temp.value != item and temp.next:
                        rear = temp
                        temp = temp.next
                    elif temp.value != item and not temp.next:
                        raise ValueError('Item is not in list!')
                    else:
                        rear.next = temp.next
                        del temp
                        break
    
    def size(self):
        if not self.head:
            return 0
        else:
            count = 1
            temp = self.head
            while temp.next != None:
                temp = temp.next
                count += 1
            return count
    
    def show(self):
        if not self.head:
            return '[]'
        else:
            result = '['
            temp = self.head
            while temp.next:
                result += (str(temp.value) + ', ')
                temp = temp.next
            result += (str(temp.value) + ']')
            return result
        
    def get_value(self, position):
        if not self.head:
            raise IndexError('List index out of range!')
        else:
            temp = self.head
            count = 1
            while count != position:
                if not temp.next:
                    raise IndexError('List index out of range!')
                temp = temp.next
                count += 1
            return temp.value
        
    def __str__(self):
        return self.show()