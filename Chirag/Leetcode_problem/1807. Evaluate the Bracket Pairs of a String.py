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

print(evaluate1("(name)is(age)yearsold",[["name","bob"],["age","two"]]))


        


        
    
