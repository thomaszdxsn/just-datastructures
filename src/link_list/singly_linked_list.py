"""
单向链表:
    index:                           O(n)
    insert/delete at beginning       O(1)
    insert/delete at end             O(1) when has tail, O(n) when not tail
    insert/delete in middle          O(1) + search time
    waste space                      O(n)


https://en.wikipedia.org/wiki/Linked_list
"""
from __future__ import annotations
from typing import Any, Iterable, Optional

import attr

__all__  = ('SinglyLinkList',)


@attr.s(slots=True, auto_attribs=True)
class Node:
    value: Any
    prev: Optional[Node] = None
    next: Optional[Node] = None


class SinglyLinkList:

    def __init__(self, iterable: Optional[Iterable] = None):
        self.length: int = 0
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None

        if iterable:
            [self.append(node) for node in iter(iterable)]

    def __len__(self):
        return self.length

    def append(self, value: Any):
        pass

    def prepend(self, value: Any):
        self.length += 1
        if not self.head:
            node = Node(value=value)
            self.head = node
            self.tail = node
            return

        node = Node(value=value, next=self.head)
        node.next.prev = node

    def insert(self, index: int, node: Node):
        pass

    def extend(self, iterable: Iterable):
        pass
