class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None      # con trỏ 2 chiều, ban đầu chưa nối ai

class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}                    # key -> Node  (LƯU NODE, không lưu value!)
        self.left, self.right = Node(0, 0), Node(0, 0)   # 2 node "lính gác"
        self.left.next, self.right.prev = self.right, self.left

    def remove(self, node):                # gỡ 1 node ra khỏi list
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev

    def insert(self, node):                # nhét node vào sát right (MỚI NHẤT)
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])   # gỡ ra
            self.insert(self.cache[key])   # nhét lại về MỚI NHẤT
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])   # có rồi thì gỡ node cũ ra
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:     # tràn?
            lru = self.left.next           # node sát left = CŨ NHẤT
            self.remove(lru)
            del self.cache[lru.key]        # xóa cả ở HashMap