class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}

        for x in s:
            freq1[x] = freq1.get(x, 0) + 1
        for x in t:
            freq2[x] = freq2.get(x, 0) + 1
        if freq1 == freq2:
            return True
        return False