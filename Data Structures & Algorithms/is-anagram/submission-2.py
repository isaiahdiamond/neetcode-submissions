class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_t = sorted(t)
        sorted_s = sorted(s)
        return sorted_t == sorted_s
    



        