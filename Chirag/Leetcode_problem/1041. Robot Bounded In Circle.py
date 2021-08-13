def isRobotBounded(instructions):
    dirx,diry=0,1
    x,y=0,0
    for i in instructions:
        if i=='G':
            x,y=x+dirx,y+diry
        elif i=='L':
            dirx,diry=-1*diry,dirx
        else:
            dirx,diry=diry,dirx*-1
    return (x,y)==(0,0) or (dirx,diry)!=(0,1)
print(isRobotBounded('GGLLGG'))
