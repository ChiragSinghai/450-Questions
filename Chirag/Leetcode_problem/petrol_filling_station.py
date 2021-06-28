def findStartingStation(P,D,n):
    total=0
    deficient=0
    start=0
    for i in range(n):
        total=total+P[i]-D[i]
        if total<0:
            start=i+1
            deficient+=total
            total=0
    return start+1 if total+deficient>=0 else -1


if __name__=='__main__':
    Petrol=[1,2,3,4,5]
    Distance=[3,4,5,1,2]
    n=len(Petrol)
    station=findStartingStation(Petrol,Distance,n)
    print(station)
