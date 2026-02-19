class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        a=set()
        count=0
        for i in words:
            rev=i[::-1]

            if rev in a:
                count+=1
            a.add(i)
        return count

        