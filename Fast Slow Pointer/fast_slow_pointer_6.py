from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()

def find_middle_of_linked_list(head):
  slow, fast = head,head
  while fast != None and fast.next != None:
    # print(fast.value)
    slow = slow.next
    fast = fast.next.next
  return slow

def reorder(head):
  if head is None or head.next is None: 
    return True
  slow = find_middle_of_linked_list(head)
  head_second_half = reverse(slow)
  next_node = None
  first_node = head
  i = 0
  while head_second_half.next is not None and head is not None:
    #detach head of second list
    next_node = head_second_half.next
    head_second_half.next = None
    # next_node.print_list()
    #attach the detacjed node to the next of the final list
    temp_node = head.next
    head.next = head_second_half
    head_second_half.next = temp_node

    head = head.next.next
    head_second_half = next_node
    if head.next == None:
      break
  return first_node

def reverse(head):
  prev = None
  while( head is not None):
    next_node = head.next
    head.next = prev
    prev = head
    head = next_node
  return prev



def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()
