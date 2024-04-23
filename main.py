"""
Author: Maxwell Tan
Date: 04/23/24
Class: CS1D
Assignment: SkipList Implementation

Description:
This Python script implements a SkipList data structure, a probabilistic alternative to balanced trees,
with support for insertion, deletion, and searching operations. SkipLists provide expected O(log n) 
performance on each operation and are particularly useful for implementing sorted dictionaries or 
sets efficiently.

The SkipList consists of SkipNodes, each containing a key-value pair and multiple forward pointers 
to nodes on lower levels. The height of each SkipNode is determined probabilistically, with higher 
nodes having fewer forward pointers, thus creating a skip effect, which allows for faster traversal 
through the list.

The SkipList class contains methods for insertion, deletion, searching, and displaying the contents 
of the SkipList. Additionally, the SkipNode class defines the structure of individual nodes in the 
SkipList.

Usage:
- Create an instance of SkipList.
- Use the insert() method to add key-value pairs.
- Use the search() method to find a value associated with a key.
- Use the delete() method to remove a key-value pair.
- Use the display() method to visualize the contents of the SkipList.

Example Usage:
skip_list = SkipList()
skip_list.insert(3, "Three")
skip_list.insert(6, "Six")
skip_list.insert(7, "Seven")
skip_list.insert(9, "Nine")
skip_list.insert(13, "Thirteen")
skip_list.insert(15, "Fifteen")

print("Skip List:")
skip_list.display()

print("\nSearching for key 7:", skip_list.search(7))
print("Searching for key 10:", skip_list.search(10))

skip_list.delete(6)
print("\nSkip List after deleting key 6:")
skip_list.display()
"""



import random

class SkipNode:
    def __init__(self, key=None, value=None, level=0):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level=16, p=0.5):
        # Initialize the skiplist with maximum level and probability p for level generation
        self.max_level = max_level
        self.p = p
        self.header = SkipNode()
        self.level = 0

    def random_level(self):
        # Generate a random level for a new node
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
      update = [None] * (self.max_level + 1)
      current = self.header
  
      for i in range(self.level, -1, -1):
          while current.forward[i] and current.forward[i].key < key:
              current = current.forward[i]
          update[i] = current
  
      current = current.forward[0]
  
      if current is None or current.key != key:
          new_level = self.random_level()
          if new_level > self.level:
              # Extend the update list if needed and initialize new levels
              for i in range(self.level + 1, new_level + 1):
                  update[i] = self.header
                  self.header.forward.append(None)  # Extend forward list of header
              self.level = new_level
  
          new_node = SkipNode(key, value, new_level)
          for i in range(new_level + 1):
              new_node.forward[i] = update[i].forward[i]
              update[i].forward[i] = new_node
  
    
  

    def search(self, key):
        # Search for a key in the skiplist
        current = self.header
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.key == key:
            return current.value
        return None

    def delete(self, key):
        # Delete a key from the skiplist
        update = [self.header] * (self.max_level + 1)
        current = self.header

        # Traverse through the skiplist to find the node to delete
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        # Move to the next node
        current = current.forward[0]

        # Check if the node exists, if yes, delete it
        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.header.forward[self.level] is None:
                self.level -= 1

    def display(self):
        # Display the skiplist
        for level in range(self.level + 1):
            print("Level {}: ".format(level), end=" ")
            node = self.header.forward[level]
            while node:
                print("{} -> ".format(node.key), end=" ")
                node = node.forward[level]
            print("None")

# Example usage
skip_list = SkipList()
skip_list.insert(3, "Three")
skip_list.insert(6, "Six")
skip_list.insert(7, "Seven")
skip_list.insert(9, "Nine")
skip_list.insert(13, "Thirteen")
skip_list.insert(15, "Fifteen")

print("Skip List:")
skip_list.display()

print("\nSearching for key 7:", skip_list.search(7))
print("Searching for key 10:", skip_list.search(10))

skip_list.delete(6)
print("\nSkip List after deleting key 6:")
skip_list.display()
