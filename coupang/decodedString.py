def decodeString(self, s):
    strStack, numStack = [], []
    length = len(s)
    tempNum = ''

    for i in range(length):
        char = s[i]
        if char.isdecimal():
            tempNum += char
        elif char == '[':
            strStack.append(char)
            numStack.append(int(tempNum))
            tempNum = ''
        elif char == ']':
            j = len(strStack) - 1
            while strStack[j] != '[':
                j -= 1
            strStack = strStack[:j] + strStack[j+1:] * numStack.pop()
        else:
            strStack.append(char)
    ''.join(strStack)

decodeString(None, '2[abc]3[cd]ef')