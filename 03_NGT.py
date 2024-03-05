def ngt(n):
    ans = []
    stack = []

    for i in n:
        while stack and stack[-1] < i:
            ans.append(i)
            stack.pop()
        stack.append(i)

    while stack:
        ans.append(-1)
        stack.pop()

    return ans

n = [4, 3, 2, 1, 5, 7, 6]
print("original array : ",n)
print(ngt(n))

