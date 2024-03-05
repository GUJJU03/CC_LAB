dic = {
    "+": 1,
    "-": 1,
    "*": 2,
    "/": 2,
}

def intopost(exp):
    operand = []
    operator = []

    for i in exp:
        if i.isalnum():
            operand.append(i)
        else:
            while operator and dic[i] < dic.get(operator[-1], 0):
                operand.append(operator.pop())
            operator.append(i)

    while operator:
        operand.append(operator.pop())  # Append the remaining operators to the operand list
    return operand

exp = "a+b/c-d"
d = intopost(exp)
print(d)       

