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

if __name__ == '__main__':
    ll = LinkedList()
    # ll.insert_at_beginning(5)
    # ll.insert_at_beginning(6)
    # ll.insert_at_beginning(8)
    # ll.insert_at_end(80)
    # ll.insert_at_end(800)
    ll.bulk_insert([1,2,45,64,0,77])
    ll.display()