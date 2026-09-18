class Node:
    """Represents one customer in the waitlist."""

    def __init__(self, name):
        self.name = name
        self.next = None


class LinkedList:
    """A singly linked list used to manage an event waitlist."""

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        return f"{name} added to the front of the waitlist"

    def add_end(self, name):
        new_node = Node(name)

        if self.head is None:
            self.head = new_node
            return f"{name} added to the end of the waitlist"

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node
        return f"{name} added to the end of the waitlist"

    def remove(self, name):
        if self.head is None:
            return f"{name} not found"

        if self.head.name == name:
            self.head = self.head.next
            return f"Removed {name} from the waitlist"

        current = self.head

        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                return f"Removed {name} from the waitlist"
            current = current.next

        return f"{name} not found"

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        print("Current waitlist:")
        current = self.head

        while current is not None:
            print(f"- {current.name}")
            current = current.next


def waitlist_generator():
    waitlist = LinkedList()

    print("--- Waitlist Manager ---")

    while True:
        print("\n1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            print(waitlist.add_front(name))

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            print(waitlist.add_end(name))

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            print(waitlist.remove(name))

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose a number from 1 to 5.")


# DESIGN MEMO
# In this program, we will be using a singly linked list in order to manage
# customers on the waitlist for events. Each individual customer will be kept
# in Node objects. Nodes keep the names of the customer and a next pointer
# that points to the next node. The LinkedList class manages nodes and gives
# methods for adding customers to the beginning or the end of the list, for
# deleting customers and for printing all of the current customers waiting.
# In case of adding customer to the beginning of the list, a new node is made
# and is pointed to the existing first node. Then, the new node becomes the
# head of the linked list. For adding customer to the end, nodes should be
# traversed to the node where the next value is None. In order to delete
# customer from the list, the program should find the corresponding node and
# update the next pointer of the previous node to skip the deleted node.
#
# The head is important for our linked list, since it is the starting node
# in our linked list. It keeps the reference to the first node, so all other
# customers can be accessed using the next pointers. When there are no
# customers in the waitlist, the head will be None. Head also needs to be
# updated when a customer is added or deleted as the first one.
#
# A custom linked structure could be used by the real engineer in case if
# there were frequent changes in the data and the program needed to control
# how the elements were linked or relinked. Waitlist for tickets is an example of
# example since the VIP customers can be added to the front of the list, while
# general customers can be added to the end.


if __name__ == "__main__":
    waitlist_generator()
