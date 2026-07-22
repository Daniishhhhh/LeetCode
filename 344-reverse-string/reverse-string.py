class Solution:
    def reverseString(self, s: List[str]) -> None:
        t= s[::-1]

        for i in range(len(s)):
            s[i]=t[i]

    
        