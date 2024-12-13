import sys
from pathlib import Path

path = Path(__file__).parent.parent
sys.path.append(str(path))

from constants import *
from node import Node

def test_node_init():
    n = Node([], None)
    assert len(n.left) == 0 and len(n.right) == 4
    assert FARMER in n.right and CABBAGE in n.right and GOAT in n.right and WOLF in n.right
    assert 1 == 2