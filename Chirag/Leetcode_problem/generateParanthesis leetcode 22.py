def generateParenthesis( n):   
    result=set()
    def dfs(curstr,x,y):
        if len(curstr)==n*2 :
            if x==y:
                result.add(curstr)
            return
    
        if y<x and y<=n:
            dfs(curstr+")",x,y+1)
            if x<=n:
                dfs(curstr+"(",x+1,y)
        else:
            dfs(curstr+"(",x+1,y)
    dfs("",0,0)
    return result
print(generateParenthesis(2))
