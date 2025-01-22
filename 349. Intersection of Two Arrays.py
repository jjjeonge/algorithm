class Solution(object):
    def intersection(self, nums1, nums2):
        dic={}
        output =[]

        for i in nums1:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        
        for i in nums2:
            if i in dic and i not in output:
                output.append(i)
        
        return output
        
