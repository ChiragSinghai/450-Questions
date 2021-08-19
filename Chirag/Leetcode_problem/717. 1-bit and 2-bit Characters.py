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
print(isOneBitCharacter([1,1,1,1,0,]))
