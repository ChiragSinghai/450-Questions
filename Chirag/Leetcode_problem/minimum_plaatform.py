def getminPlatform(arrival,depart):
    arrival.sort()
    depart.sort()
    min_platform = 1
    min_platform_till_now = 1
    i=1
    j=0
    n=len(arrival)
    while i < n and j < n:
        if arrival[i]<depart[j]:
            min_platform_till_now +=1
            i+=1
        elif arrival[i] > depart[j]:
            min_platform_till_now -= 1
            j+=1
        if min_platform_till_now > min_platform:
            min_platform = min_platform_till_now
    print(min_platform)
        

if __name__=='__main__':
    A=[900, 940, 950, 1100, 1500, 1800]
    B=[910, 1200, 1120, 1130, 1900, 2000]
    getminPlatform(A,B)
