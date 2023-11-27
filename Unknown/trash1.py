def values():
    value = 0
    while True:
        value += 1
        yield value
        yield -1 * value


class Trash:
    _hash_iter = values()

    def __hash__(self):
        tmp = Trash._hash_iter.__next__()
        return tmp


if __name__ == "__main__":
    #trash = Trash()
    trash = "trash"
    print(f"equals: {trash == trash}")
    trash_set = set()
    trash_set.add(trash)
    trash_set.add(trash)
    print(f"set: {trash_set}")
    trash_list = list(trash_set)
    print(f"list: {trash_list}")
    # print(f"final test: {trash_list[0] == trash_list[1]}")
