#create nodes
#create linked list
#Add nodes to linkedlist
#Print linked list

class Node:
  def __init__(self,data):
    self.data=data
    self.next=None

class LinkedList:
  def __init__(self):
    self.head=None

  def insert(self,new_node):
    if self.head is None:
      self.head = new_node
    else:
      last_node = self.head
      while last_node.next is not None:
        last_node=last_node.next
      last_node.next = new_node


  def insert_node_as_head(self,node_at_head):
    temp_node=self.head
    self.head=node_at_head
    node_at_head.next=temp_node

  def printList(self):
    # head=>John->Ben->Mathew
    current_node=self.head
    if current_node is None:
      print("Nothing is there in linkedList")
    else:
      while current_node is not None:
        print(current_node.data)
        current_node=current_node.next

  def llistlength(self):
    count=0
    current_node=self.head
    while current_node is not None:
      count+=1
      current_node=current_node.next
    return count

  def insert_node_in_between(self,node_in_between,index_val):
    
    if index_val == 0:
      linkedList.insert_node_as_head(node_in_between)
    if index_val < 0 or index_val > self.llistlength():
      print("Invalid Value")
      
    count=0
    current_node=self.head
    while current_node is not None:
      count+=1
      if count==index_val-1:
        previous_node=current_node
      if count==index_val:
        previous_node.next=node_in_between
        node_in_between.next=current_node   
      current_node=current_node.next

  def index_of_node_to_be_removed(self,node_to_be_removed):
    count=0
    current_node=self.head
    while current_node is not None:
      count+=1
      if current_node.data == node_to_be_removed:
        return count
      current_node=current_node.next
      

  def delete_node(self,node_to_be_removed):
      count=0
      #print(node_to_be_removed)
      index_of_node_to_be_removed=linkedList.index_of_node_to_be_removed(node_to_be_removed)
      #print(index_of_node_to_be_removed)
      current_node=self.head
      while current_node is not None:
        count+=1
        if index_of_node_to_be_removed-1 == count:
          previous_node=current_node
        if index_of_node_to_be_removed == count:
          previous_node.next=None
        if index_of_node_to_be_removed+1 == count:
          next_elem=current_node
          previous_node.next=next_elem
        current_node=current_node.next  

#node = data,next
firstNode = Node("John")
linkedList = LinkedList()
linkedList.insert(firstNode)

secondNode = Node("Ben")
linkedList.insert(secondNode)

thirdNode = Node("Matthew")
linkedList.insert(thirdNode)

node_at_head = Node("Amit")
linkedList.insert_node_as_head(node_at_head)

node_at_head = Node("Kajal")
linkedList.insert_node_as_head(node_at_head)

node_in_between = Node("Aanchal")
linkedList.insert_node_in_between(node_in_between,2)

linkedList.delete_node("Aanchal")

linkedList.printList()




