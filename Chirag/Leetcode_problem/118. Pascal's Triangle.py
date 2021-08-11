def printmat(dp):
    for row in dp:
        print(row)

def generate(numRows):
        matrix=[[1]]
        for i in range(1,numRows):
            temp=[0]+matrix[-1]+[0]
            for j in range(i+1):
                temp[j]=temp[j]+temp[j+1]
            matrix.append(temp[:i+1])
        return matrix
#fast method
def generate1(numRows):
        if numRows==1:
            return [[1]]
        matrix=[[1],[1,1]]
        for i in range(2,numRows):
            temp=[]
            for j in range(i-1):
                temp.append(matrix[i-1][j]+matrix[i-1][j+1])
            matrix.append([1]+temp+[1])
        return matrix

def generate2(numRows):
        dp = [[1] * i for i in range(1,numRows+1)]
        
        for i in range(numRows):
            for j in range(i+1):
                if not(j == 0 or j == i):
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    
        return dp
printmat(generate2(5))
