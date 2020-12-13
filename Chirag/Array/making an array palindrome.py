def PalinArray(arr ,n):
    for i in arr:
        i=str(i)
        if i[::-1]==i:
            continue
        else:
            return 0
    return 1


if __name__=='__main__':
    PalinArray([],n)
