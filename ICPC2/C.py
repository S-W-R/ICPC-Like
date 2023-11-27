from typing import Dict, List


class PrefixTree:
    def __init__(self, char: str):
        self.char = char
        self.inner_count: int = 0
        self.next_nodes: Dict[str, PrefixTree] = dict()
        self.prev_node: PrefixTree = None

    def add_file(self, filename):
        current_node = self
        while filename != '':
            current_node.inner_count += 1
            first_char = filename[0]
            if first_char in current_node.next_nodes:
                next_n = current_node.next_nodes[first_char]
            else:
                next_n = PrefixTree(first_char)
                current_node.next_nodes[first_char] = next_n
            next_n.prev_node = current_node
            current_node = next_n
            filename = filename[1:]
        current_node.inner_count += 1

    def __repr__(self):
        return "'" + self.char + "':" + str(self.inner_count)

split_char = ' '
(count, max_files) = [int(x) for x in input().split()]
tree = PrefixTree('')
for p in range(count):
    raw = input()
    tree.add_file(raw)

result = 0
while tree.inner_count > 0:
    visited: List[PrefixTree] = []
    current = tree
    while current is not None:
        visited.append(current)
        if current.inner_count <= max_files:
            result += 1
            deleted = current.inner_count
            for i in visited:
                i.inner_count -= deleted
            break
        optimal_node = None
        new_node = None
        max_count = 0
        for v in current.next_nodes.values():
            c = v.inner_count
            if c <= 0:
                continue
            if c == max_files:
                optimal_node = v
            if c > max_count:
                max_count = c
                new_node = v
        if optimal_node is not None:
            current = optimal_node
        else:
            current = new_node
print(result)
