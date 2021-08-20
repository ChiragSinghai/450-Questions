def isOneBitCharacter(bits):
    prev=-1
    while bits:
        next=bits.pop(0)
        if prev==1 and (next==0 or next==1):
            next=prev=-1
        elif prev==-1 and next==0:
            if not bits:
                return True
            prev=-1
        else:
            prev=next
    return False
def isOneBitCharacter1(bits):
    if bits==[0]:
        return True
    elif bits==[1]:
        return False
    if bits[-1]==0 and bits[-2]==0:
        return True
    count=0
    if bits[-1]==0 and bits[-2]==1:
        for i in bits[-2::-1]:
            if i!=1:
                break
            count+=1
        if not count & 1:
            return True
    return False
print(isOneBitCharacter1([1,1,1,1,0,]))
