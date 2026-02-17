def calculate(expression: str) -> float:
    s = expression.replace(" ", "")
    stack = []
    num = 0
    sign = '+'
    i = 0
    while i < len(s):
        if s[i].isdigit() or (s[i] == '-' and (i == 0 or s[i-1] in '+-*/')):
            neg = False
            if s[i] == '-':
                neg = True
                i += 1
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            if neg:
                num = -num
            if sign == '+':
                stack.append(num)
            elif sign == '-':
                stack.append(-num)
            elif sign == '*':
                stack.append(stack.pop() * num)
            elif sign == '/':
                stack.append(stack.pop() / num)
            continue
        else:
            sign = s[i]
        i += 1
    return round(sum(stack), 2)

if __name__ == "__main__":
    print(calculate("2 + 3"))
    print(calculate("10 - 5 * 2"))
    print(calculate("20 / 4 + 3 * 2"))
    print(calculate("100 / 3"))
    print(calculate("5"))

    assert calculate("2 + 3") == 5.0
    assert calculate("10 - 5 * 2") == 0.0
    assert calculate("20 / 4 + 3 * 2") == 11.0
    assert calculate("100 / 3") == 33.33
    assert calculate("5") == 5.0

    print("All test cases passed")
