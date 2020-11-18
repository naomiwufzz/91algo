class HashDoubleLinkedNode(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None



class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        hash_double_lined_node = HashDoubleLinkedNode()



    def get(self, key: int) -> int:


    def put(self, key: int, value: int) -> None:



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)