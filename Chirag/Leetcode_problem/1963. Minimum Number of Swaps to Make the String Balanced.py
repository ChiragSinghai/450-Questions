class Solution:
    def minSwaps(self, s) :
        closing=0
        opening=0
        for bracket in s:
            if bracket=='[':
                opening+=1
            else:
                if not opening:
                    closing+=1
                else:
                    opening-=1
        return (closing+1)//2
obj=Solution()
print(obj.minSwaps('[[[[[]]]]]'))
