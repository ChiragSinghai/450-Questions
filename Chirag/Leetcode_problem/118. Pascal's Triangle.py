def generate(numRows):
        matrix=[[1]]
        for i in range(1,numRows):
            temp=[0]+matrix[-1]+[0]
            for j in range(i+1):
                temp[j]=temp[j]+temp[j+1]
            matrix.append(temp[:i+1])
        return matrix
def printmat(dp):
    for row in dp:
        print(row)
printmat(generate(5))
