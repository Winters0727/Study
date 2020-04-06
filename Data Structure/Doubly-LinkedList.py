class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value
        self.next = None

class DLinkedList: # list to DLinkedList
    def __init__(self, inp_list, head=None, tail=None):
        self.head = head
        self.tail = tail
        for i in range(len(inp_list)):
            if i == 0 and not self.head:
                N = Node(inp_list[i])
                self.head = N
            else:
                if i == len(inp_list)-1 and not self.tail:
                    next_N = Node(inp_list[i])
                    N.next = next_N
                    next_N.prev = N
                    self.tail = next_N
                else:
                    next_N = Node(inp_list[i])
                    N.next = next_N
                    next_N.prev = N
                    N = next_N
    
    def __len__(self):
        if not self.head:
            return 0
        else:
            N = self.head
            cnt = 1
            while N != self.tail:
                N = N.next
                cnt += 1
            return cnt

    def __str__(self):
        if not self.head:
            return '[]'
        else:
            N = self.head
            result = str(N.value)
            while N != self.tail:
                N = N.next
                result += ', ' + (str(N.value))
            return ('[' + result + ']')