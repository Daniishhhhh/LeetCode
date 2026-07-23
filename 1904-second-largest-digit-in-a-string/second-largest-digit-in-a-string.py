class Solution:
    def secondHighest(self, s: str) -> int:
        st=list(s)
        lis=[]
        for i in range(len(st)):
            if st[i].isdigit():
                lis.append(int(st[i]))
        lis=list(set(lis))
        lis.sort()
        if len(lis)<2:
            return -1
        return lis[-2]
        
        
        