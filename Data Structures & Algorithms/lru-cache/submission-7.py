class Node:
  def __init__(self, key, val, next=None, prev=None):
    self.val = val
    self.key = key
    self.next = next
    self.prev = prev


class LRUCache:

  def __init__(self, capacity: int):
    self.cap = capacity
    self.node_storage = {}
    self.head_ptr = None
    self.tail_ptr = None

  def print_cache(self):
    curr = self.head_ptr
    while curr:
      print(curr.val)
      curr = curr.next

  # make node head of list
  def insert(self, node):

    node.next = self.head_ptr
    node.prev = None
    if self.head_ptr:
      self.head_ptr.prev = node
    self.head_ptr = node
    if not self.tail_ptr:  # If the list was empty, set tail
      self.tail_ptr = node

  # remove node from list
  def remove(self, node):
    # Remove node from the linked list
    if node.prev:
        node.prev.next = node.next
    if node.next:
        node.next.prev = node.prev

    # Update head and tail pointers if needed
    if self.head_ptr == node:  # If it's the head
        self.head_ptr = node.next
    if self.tail_ptr == node:  # If it's the tail
        self.tail_ptr = node.prev

    # Clean up the node
    node.prev = None
    node.next = None

  def get(self, key: int) -> int:
    if key not in self.node_storage:
      return -1

    key_node = self.node_storage[key]
    value = key_node.val

    # remove node
    self.remove(key_node)

    # re-add node
    self.put(key, value)

    return value

  def put(self, key: int, value: int) -> None:
    # find existing node, remove then re-add to list
    if key in self.node_storage:
      node = self.node_storage[key]
      node.val = value
      self.remove(node)
      self.insert(node)
      return

    # full... remove tail then add new node
    if len(self.node_storage) >= self.cap:
      del self.node_storage[self.tail_ptr.key]
      self.remove(self.tail_ptr)

    # completely new, add to list
    node = Node(key, value)
    self.insert(node)
    self.node_storage[key] = node
