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

__all__ = ('SinglyLinkList',)


@attr.s(slots=True, auto_attribs=True)
class Node:
    value: Any
    prev: Optional[Node] = None
    next: Optional[Node] = None

    def __str__(self):
        return str(self.value)


class SinglyLinkList:

    def __init__(self, iterable: Optional[Iterable] = None):
        self.length: int = 0
        self._head: Optional[Node] = None
        self._tail: Optional[Node] = None

        if iterable:
            [self.append(node) for node in iter(iterable)]

    def __len__(self):
        return self.length

    def __iter__(self):
        node = self._head
        while node:
            yield node.value
            node = node.next

    @property
    def tail(self) -> Optional[any]:
        """return tail's value if exists"""
        return self._tail and self._tail.value

    @property
    def head(self) -> Optional[any]:
        """return head's value if exists"""
        return self._head and self._head.value

    def _add_head(self, value: Any):
        assert not self.head, 'can\'t add head when head exists'
        node = Node(value=value)
        self._head = node
        self._tail = node
        self.length += 1

    def append(self, value: Any):
        if not self.head:
            self._add_head(value)
            return
        self.length += 1
        node = Node(value=value, prev=self._tail)
        node.prev.next = node
        self._tail = node

    def prepend(self, value: Any):
        if not self.head:
            self._add_head(value)
            return
        self.length += 1
        node = Node(value=value, next=self._head)
        node.next.prev = node
        self._head = node

    def insert(self, index: int, node: Node):
        # TODO: must implementation __getitem__ API
        pass

    def extend(self, iterable: Iterable[Any]):
        for item in iterable:
            self.append(item)
