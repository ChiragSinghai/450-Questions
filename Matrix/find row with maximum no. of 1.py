class Solution:
    def binary(self,arr,m):
        
        i=0
        while i<=m:
            mid=(i+m)//2
            #print(mid)
            if (mid==0 or arr[mid-1]==0) and arr[mid]==1:
                return mid
            elif(arr[mid]==0):
                i=mid+1
            else:
                m=mid-1
            #print(mid)
        return -1
    
    def rowWithMax1s(self,arr, n, m):
        row=0
        ma=self.binary(arr[0],m-1)
        #print(ma)
        for i in range(1,n):
            if arr[i][ma]==1 & ma!=-1:
                index=self.binary(arr[i],ma)
                #print(index,row,i)
                if index!=-1 and index<ma:
                    ma=index
                    row=i
            if ma==-1:
                ma=self.binary(arr[i],m-1)
        print(row)
if __name__=='__main__':
    arr=[[0,1,1,1],
         [0,0,1,1],
         [0,1,1,1],
         [0,0,0,0],
         [1,1,1,1]]
    n=5
    m=4
    obj=Solution()
    obj.rowWithMax1s(arr,n,m)



    
