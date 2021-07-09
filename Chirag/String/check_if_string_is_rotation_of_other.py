def check(s1,s2):
    s1=s1*2
    return True if s2 in s1 else False
if __name__=='__main__':
    S1='abcdef'
    S2='cdefam'
    print(check(S1,S2))
