class RecentCounter:

    def __init__(self):
        self.requests = []
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] < t - 3000:
            self.requests.pop(0)
        return len(self.requests)

recentCounter = RecentCounter()

print(recentCounter.ping(1))

print(recentCounter.ping(100))

print(recentCounter.ping(3001))

print(recentCounter.ping(3002))

# Output: null, 1, 2, 3, 3