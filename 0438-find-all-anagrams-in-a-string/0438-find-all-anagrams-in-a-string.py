class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        from collections import Counter
        p_count=Counter(p)
        wind_count=Counter()
        left=0
        result=[]
        for right in range (len(s)):
            wind_count[s[right]]+=1
            if right-left+1 > len(p):
                wind_count[s[left]]-=1
                if wind_count[s[left]]==0:
                    del wind_count[s[left]]
                left+=1
            if wind_count==p_count:
                result.append(left)

        return result

        