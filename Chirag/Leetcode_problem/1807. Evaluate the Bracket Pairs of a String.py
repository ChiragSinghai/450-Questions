def evaluate( s, knowledge):
    d = dict(knowledge)
    a = lambda x: d.get(x.group(0)[1:-1], '?')
    return re.sub('\([a-z]+\)', a, s)
print(evaluate("(name)is(age)yearsold",[["name","bob"],["age","two"]]))

        


        
    
