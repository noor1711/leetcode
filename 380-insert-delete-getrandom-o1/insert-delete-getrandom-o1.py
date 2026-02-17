import random
class RandomizedSet:

    def __init__(self):
        random.seed(17)
        self.arr = []
        self.dic = {}

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        self.dic[val] = len(self.arr)
        self.arr.append(val)

        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.dic:
            return False
        
        index = self.dic[val]
        self.arr[index] = self.arr[-1]
        self.dic[self.arr[-1]] = index
        self.arr.pop()
        del self.dic[val]
        return True

    def getRandom(self) -> int:
        index = random.randrange(len(self.arr))
        return self.arr[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()