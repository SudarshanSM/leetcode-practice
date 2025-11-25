class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels=set('aeiouAEIOU')
        a=[ch for ch in s if ch in vowels]

        result=[]
        for ch in s:
            if ch in vowels:
                result.append(a.pop())
            else:
                result.append(ch)

        return "".join(result)

        