class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # HashMap 만들기
        dic ={}

        #iterate
        #a-2,b-1 이런식..
        for i in magazine:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        #iterate & 있으면 감소시키기
        for j in ransomNote:
            if j in dic and dic[j] > 0:
                dic[j] -=1
            else:
                return False
        
        return True
