def letterCombinations(digits):
    digToChar={'2':'abc',
              '3':'def',
              '4':'ghi',
              '5':'jkl',
              '6':'mno',
              '7':'pqrs',
              '8':'tuv',
              '9':'wxyz'}
    result = []
    def dfs(i,currstr):
        if i>=len(digits):
            result.append(currstr)
            return
        for c in digToChar[digits[i]]:
            dfs(i+1,currstr+c)
    if digits:
        dfs(0,"")
    return result
print(letterCombinations("45"))
