class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counts = 0
        for s in jewels:
            counts += stones.count(s)
        return counts
        