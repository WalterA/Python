# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next
class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
def stampa_lista(head: ListNode):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

# Creazione delle liste di test
# Lista 1: [1, 2, 3, 4, 5]
nodo1 = ListNode(1)
nodo2 = ListNode(2)
nodo3 = ListNode(3)
nodo4 = ListNode(4)
nodo5 = ListNode(5)
nodo1.next = nodo2
nodo2.next = nodo3
nodo3.next = nodo4
nodo4.next = nodo5

# Lista 2: [10, 20, 30]
nodo6 = ListNode(10)
nodo7 = ListNode(20)
nodo8 = ListNode(30)
nodo6.next = nodo7
nodo7.next = nodo8

# Lista 3: [7]
nodo9 = ListNode(7)

# Lista 4: []
nodo10 = None

# Creazione dell'oggetto Solution
soluzione = Solution()

# Test 1: Lista 1
print("Test 1: Lista [1, 2, 3, 4, 5]")
stampa_lista(nodo1)
test1_risultato = soluzione.reverseList(nodo1)
stampa_lista(test1_risultato)

# Test 2: Lista 2
print("Test 2: Lista [10, 20, 30]")
stampa_lista(nodo6)
test2_risultato = soluzione.reverseList(nodo6)
stampa_lista(test2_risultato)

# Test 3: Lista 3
print("Test 3: Lista [7]")
stampa_lista(nodo9)
test3_risultato = soluzione.reverseList(nodo9)
stampa_lista(test3_risultato)

# Test 4: Lista 4 (vuota)
print("Test 4: Lista vuota")
stampa_lista(nodo10)
test4_risultato = soluzione.reverseList(nodo10)
stampa_lista(test4_risultato)

# 876. Middle of the Linked List
class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        array: list = []
        
        while head:
            array.append(head.val)
            head = head.next
            
        middle_index: int = len(array) // 2
        result = ListNode(array[middle_index])
        current = result
        for val in array[middle_index + 1:]:
            current.next = ListNode(val)
            current = current.next
        return result

# 3217. Delete Nodes From Linked List Present in Array
class Solution:
    def modifiedList(self, nums: list[int], head: ListNode) -> ListNode:
        nums = set(nums)
        pippo = ListNode(0)
        pippo.next = head
        current_node = pippo
        while current_node.next:
            if current_node.next.val in nums:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        return pippo.next
    
    