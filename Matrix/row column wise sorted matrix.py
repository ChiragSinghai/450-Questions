def fun():
    pass
'''
2
4
10 20 30 40 15 25 35 45 27 29 37 48 32 33 39 50
3
1 3 4 2 6 7 5 8 9
'''
if __name__=='__main__':
    for _ in range(int(input())):
        n=int(input())
        l=list(map(int,input().split()))
        l.sort()
        for i in l:
            print(i,end=' ')
        print()
