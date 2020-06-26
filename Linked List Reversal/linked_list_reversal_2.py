from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()


def reverse_sub_list(head, p, q):
  # TODO: Write your code here 
  if head.value == p:
    prev_pointer = None
  else:
    prev_pointer = head
    head = head.next

  while head != None:
    if head.value != p:
      prev_pointer = prev_pointer.next
    else:
      head = reverse(head,q)
      break
  prev_pointer.next = head
  return prev_pointer

def reverse(head,q):
  # TODO: Write your code here
  end = None
  end_list = head
  reverser = head
  while head.value != q:
    head = head.next
    reverser.next = end
    end = reverser
    reverser = head
  head = head.next
  reverser.next = end
  end = reverser
  reverser = head
  end_list.next = head
  return end


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()
main()
