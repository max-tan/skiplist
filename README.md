# SkipList Implementation in Python

This repository contains a Python implementation of the SkipList data structure, a probabilistic alternative to balanced trees. SkipLists are efficient for implementing sorted dictionaries or sets, offering expected O(log n) performance for insertion, deletion, and search operations.

## Overview

SkipList is a data structure that allows fast search, insert, and delete operations. It is built upon multiple levels of linked lists, where each node could skip several nodes ahead, hence the name "SkipList". This implementation offers an easy-to-understand example of how SkipLists work under the hood.

## Features

- **Insertion**: Add key-value pairs to the SkipList.
- **Search**: Efficiently find the value associated with a given key.
- **Deletion**: Remove key-value pairs from the SkipList.
- **Display**: Visualize the structure of the SkipList for debugging and understanding.

## Usage

To use this SkipList implementation, first, create an instance of `SkipList`, then utilize its methods (`insert`, `search`, `delete`, `display`) to manipulate the SkipList.

### Example

```python
from path.to.skplist import SkipList

# Create a SkipList instance
skip_list = SkipList()

# Insert elements
skip_list.insert(3, "Three")
skip_list.insert(6, "Six")
...

# Search for an element
print("Searching for key 7:", skip_list.search(7))

# Delete an element
skip_list.delete(6)

# Display the SkipList
skip_list.display()
