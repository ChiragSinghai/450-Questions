class ProductOfNumbers:

    def __init__(self):
        self.nums=[]
        self.product=[]
        self.zero=-1
        self.count=0
        
    def add(self, num: int) -> None:
        
        self.nums.append(num)
        if not num:
            self.zero=max(self.zero,self.count)
        self.count+=1
        if not self.product:
            self.product.append(num or 1)
                    
        else:
            self.product.append((num*self.product[-1]) or 1) 
            
        
    def getProduct(self, k: int) -> int:
        if self.count-self.zero<=k:return 0
        if k==len(self.nums):
            return self.product[-1]
        return self.product[-1]//self.product[-k-1]
    
##new solution
class ProductOfNumbers:

    def __init__(self):
        self.nums=[]
        self.product=[]
        self.zero=-1
        self.count=0
        
    def add(self, num: int) -> None:
        
        self.nums.append(num)
        if num==1:
            self.count+=1
            self.product.append(self.product[-1] if self.product else 1)
            return
        if not num:
            self.zero=max(self.zero,self.count)
        self.count+=1
        if not self.product:
            self.product.append(num or 1)
                    
        else:
            self.product.append((num*self.product[-1]) or 1) 
            
        
    def getProduct(self, k: int) -> int:

        if self.count-self.zero<=k and self.zero!=-1:return 0
        if k==len(self.nums):
            return self.product[-1]
        return self.product[-1]//self.product[-k-1]
