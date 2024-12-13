from __future__ import annotations
from typing import Optional, List, Iterator
from constants import *

class Node:
    def __init__(self, left: List[str], parent: Optional[Node]) -> None:
        self.left: List[str] = sorted(left)
        self.right: List[str] = []
        self.parent: Optional[Node] = parent

        for item in items:
            if item not in self.left:
                self.right.append(item)

    def __str__(self) -> str:
        return f'<{"".join(self.left)} || {"".join(self.right)}>'

    __repr__ = __str__

    def __eq__(self, other):
        return self.left == other.left

    def is_solution(node) -> bool:
        return len(node.right) == 4 and len(node.left) == 0

    def print_path(self) -> None:
        print(self)
        if self.parent is None:
            return
        else:
            self.parent.print_path()

    def get_successors(self) -> Iterator[Node]:
        for item in self.left if FARMER in self.left else self.right:
            new_node = Node(self.left[:], self)
            list_with_farmer: List[str] = new_node.left if FARMER in new_node.left else new_node.right
            list_without_farmer: List[str] = new_node.left if FARMER not in new_node.left else new_node.right

            list_with_farmer.remove(FARMER)
            list_without_farmer.append(FARMER)
            if item != FARMER:
                list_with_farmer.remove(item)
                list_without_farmer.append(item)

            if new_node.is_valid():
                new_node.left = sorted(new_node.left)
                new_node.right = sorted(new_node.right)
                yield new_node

    def is_valid(self) -> bool:
        for bank in [self.left, self.right]:
            if GOAT in bank and (WOLF in bank or CABBAGE in bank) and FARMER not in bank:
                return False
        return True

    def is_repeated(self):
        ancestor = self.parent
        while ancestor is not None:
            if self == ancestor:
                return True
            ancestor = ancestor.parent
        return False