class MyHashMap:

    def __init__(self):
        self.new_list = []

    def put(self, key: int, value: int) -> None:
        for s in self.new_list:
            if s[0] == key:
                s[1] = value
                return
        self.new_list.append([key, value])
        

    def get(self, key: int) -> int:
        for s in self.new_list:
            if s[0] == key:
                return s[1]
        return -1


    def remove(self, key: int) -> None:
        for s in self.new_list:
            if s[0] == key:
                self.new_list.remove(s)
                return
                
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)