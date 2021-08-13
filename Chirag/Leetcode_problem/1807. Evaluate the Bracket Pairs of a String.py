import re
def evaluate( s, knowledge):
    d = dict(knowledge)
    a = lambda x: d.get(x.group(0)[1:-1], '?')
    return re.sub('\([a-z]+\)', a, s)
def evaluate1(s,knowledge):
    graph = {x[0] : x[1] for x in knowledge}
    stack, result = [], ""
    for c in s:
        if c not in '()':
            if not stack: result += c
            else: stack.append(c)

        elif c == '(':
            stack.append('(')

        elif c == ')':
            key = ''.join(stack)[1:]
            result += graph.get(key, '?')
            stack.clear()
    return result
def evaluate2(s,knowledge):    
    D={k:v for k,v in knowledge}
    while True:
        matches=re.search(r'(\([a-z]*\))',s)
        #print(s,matches)
        if matches:
            m='\('+matches.group()+'\)'
            
            
            s=re.sub(m,D.get(s[matches.start()+1:matches.end()-1],'?'),s)
        else:
            return s
def evaluate3(s,knowledge):
    D={k:v for k,v in knowledge}
    l=0
    r=0
    i=0
    n=len(s)
    res=''
    found=False
    

    while i<n:
        if s[i]=='(':
            l=i
            found=True
        elif s[i]==')':
            r=i
            found=False
        elif not found:
            res+=s[i]
        if r and l!=r:
            #print(s[l+1:r])
            res+=D.get(s[l+1:r],'?')
            #del D[s[l+1:r]]
            l=0
            r=0
        i+=1
    return res

print(evaluate1("(name)is(age)yearsold",[["name","bob"],["age","two"]]))


        


        
    
