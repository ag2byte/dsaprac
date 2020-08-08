class HS:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __hash__(self):
        return hash((self.key, self.value))


a = HS(5, "hello")
b = HS(6, "byte")
c = HS(8, "not")

print(hash(a), hash(b), hash(c))
