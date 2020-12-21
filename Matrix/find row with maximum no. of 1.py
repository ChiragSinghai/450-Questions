class Solution:
    def binary(self,arr,m):
        try:
            i=0
            while i<=m:
                mid=i+(m-i)//2
                if (mid==0 or arr[mid-1]==0) and arr[mid]==1:
                    return mid
                elif(arr[mid]==0):
                    i=mid+1
                else:
                    m=mid-1
            return -1
        except:
            print(mid)
    def rowWithMax1s(self,arr, n, m):
        row=0
        ma=self.binary(arr[0],m-1)
        for i in range(1,n):
            #print(row,i)
            if arr[i][ma]==1 & ma!=-1:
                index=self.binary(arr[i],m-1)
                print(index,row,i)
                if index!=-1 and C-index>ma:
                    ma=C-index
                    row=i
            else:
                ma=self.binary(arr[i],m-1)
        print(row)
if __name__=='__main__':
    arr=[[0,1,1,1],
         [0,0,1,1],
         [1,1,1,1],
         [0,0,0,0]]
    n=4
    m=4
    obj=Solution()
    obj.rowWithMax1s(arr,n,m)



    
