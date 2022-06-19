class Node:
  value = ""
  children = []

  def __init__(self, val):
    self.value = val

  def addChild(self, child):
    self.children.append(Node(child))


def preOrder(node: Node) -> None:
  print(node.value + " ")
  if(len(node.children)):
    for i in node.children:
      preOrder(i)
