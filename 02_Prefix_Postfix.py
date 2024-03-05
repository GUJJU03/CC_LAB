def postfix(exp):
    exp=exp.split()
    stack=[]

    for i in exp:
        if i not in "/*+-":
            stack.append(int(i))
        else:
            r=stack.pop()
            l=stack.pop()

            if i=="+":
                stack.append(r+l)
            elif i=="-":   
                stack.append(r-l)
            elif i=="*":   
                stack.append(r*l)
            elif i=="/":   
                stack.append(r/l)
            return stack.pop()
        
e = "2 3 4 5 * /"
print("Value of postfix : ",postfix(e))
 


 