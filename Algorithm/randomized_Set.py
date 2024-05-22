import random

class RandomizedSet:

    def __init__(self):
        self.observe = {}
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        self.observe[val] = len(self.values)
        self.values.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values:
            return False
        index = self.observe[val]
        last_val = self.values[-1]
        self.values[index] = last_val
        self.observe[last_val] = index
        self.observe[last_val] = self.observe[val]
        del self.observe[val]
        self.values.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()