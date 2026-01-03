class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a=list(s)
        for ch in t:
            if ch in a:
                a.remove(ch)
            else:
                return False
        return True