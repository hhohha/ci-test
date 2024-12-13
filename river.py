from node import Node
from constants import *

nodes_count = 0

def main() -> None:
    qopen: List[Node] = []
    solutions = 0

    qopen.append(Node([FARMER, CABBAGE, GOAT, WOLF], None))

    while qopen:
        node = qopen.pop(0)

        if node.is_solution():
            node.print_path()
            print('-------------------')
            solutions += 1

        for new_node in node.get_successors():
           if not new_node.is_repeated():
                qopen.append(new_node)

    print(f'found solutions: {solutions}')
    print(f'nodes count: {nodes_count}')

if __name__ == '__main__':
    main()