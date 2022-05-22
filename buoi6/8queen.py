from mimetypes import init


class Node:
  def __init__(self, dat) -> None:
    self.data = dat
    self.next = None

  def delete(self):
    self.next = self.next.next

  def insert(self, n):
    n.next = self.next
    self.next = n

class StartList:
  def __init__(self) -> None:
    self.head = Node(None)

  def length(self):
    e = self.head
    k = 1
    while(e.next != None):
      k += 1
      e = e.next
    return k

  def printList(self):
    e = self.head
    while(e.next != None):
      print(e.data)
      e = e.next
    print(e.data)

  def insert(self, n: Node):
    e = self.head
    while(e.next != None):
      e = e.next
    e.next = n

  def insertBefore(self, n: Node):
    n.next = self.head
    self.head = n

  def pop(self):
    e = self.head
    while(e.next.next != None):
      e = e.next
    e.next = None


list1 = StartList()
list1.head = Node(1)
e2 = Node(2)
e3 = Node(3)
list1.head.next = e2
e2.next = e3
list1.insertBefore(Node(0))
list1.pop()
list1.printList()
