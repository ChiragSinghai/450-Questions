# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        if n==1:
            return n if isBadVersion(n) else 0
        def binary_search(l,r):
            if l<r:
                m=(l+r)//2
                if r-l==1:
                    return l if isBadVersion(l) else r
                elif isBadVersion(m):
                    return binary_search(l,m)
                else:
                    return binary_search(m,r+1)
        return binary_search(1,n)
        """
        :type n: int
        :rtype: int
        """
        
