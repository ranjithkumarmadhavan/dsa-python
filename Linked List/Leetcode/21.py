class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, data=None):
        self.head = data

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_beginning(data)
            return
        
        dummy = self.head
        if dummy.next is None:
            dummy.next = Node(data, None)
            return

        while dummy.next:
            dummy = dummy.next
            if dummy.next is None:
                dummy.next = Node(data, None)
                return

    def bulk_insert(self, data_list):
        for data in data_list:
            self.insert_at_end(data)
        
    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        
        dummy = self.head
        ll_str = f"{dummy.data} --> "

        while dummy.next:
            ll_str += f"{dummy.next.data} --> "
            dummy = dummy.next

        print(ll_str)

class Solution:
    def mergeTwoLists(self, list1, list2):
        node = Node()
        dummy = node

        while list1.data and list2.data:
            if list1.data <= list2.data:
                dummy.head = list1.data



if __name__ == '__main__':
    ll = LinkedList()
    ll.bulk_insert([1,2,4])
    ll.display()

    ll2 = LinkedList()
    ll2.bulk_insert([1,3,4])
    ll2.display()

