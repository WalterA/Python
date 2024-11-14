class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.target=k
        self.lista=nums

    def add(self, val: int) -> int:
        self.lista.append(val)
        self.lista.sort(reverse=True)
        return self.lista[self.target-1]
    