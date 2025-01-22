class Solution(object):
    def intersect(self, nums1, nums2):
        num1=sorted(nums1)
        num2=sorted(nums2)

        i=0
        j=0

        output=[]

        while i<len(num1) and j< len(num2):
            if num1[i] < num2[j]:
                i+=1
            elif num2[j] < num1[i]:
                j+=1
            else:
                output.append(num1[i])
                i+=1
                j+=1
        return output
