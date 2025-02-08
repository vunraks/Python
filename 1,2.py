#1
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         last = self.head
#         while last.next:
#             last = last.next
#         last.next = new_node
    
#     def length(self):
#         count = 0
#         current = self.head
#         while current:
#             count += 1
#             current = current.next
#         return count

# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# print(llist.length())




#2
def fibonacci(n):
    if n <= 0:
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

def reverse_string(s):
    return s[::-1]

def count_elements(lst):
    return len(lst)

print(fibonacci(10))
print(reverse_string("hello"))
print(count_elements([1, 2, 3, 4, 5]))
