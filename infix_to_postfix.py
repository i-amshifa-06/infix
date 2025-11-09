def infix_to_postfix(exp):
    p = {'+':1,'-':1,'*':2,'/':2}
    s = []
    post = ""
    for ch in exp:
        if ch.isalnum():
            post += ch
        elif ch == '(':
            s.append(ch)
        elif ch == ')':
            while s[-1] != '(':
                post += s.pop()
            s.pop()
        else:
            while s and s[-1] != '(' and p[ch] <= p.get(s[-1],0):
                post += s.pop()
            s.append(ch)
    while s:
        post += s.pop()
    return post

print(infix_to_postfix("a+(b*c-d)/e"))
