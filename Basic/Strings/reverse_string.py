def reverseString(str):
    strArr = str.split(" ")
    resultStr = ""
    for i in range(1, len(strArr) + 1):
        resultStr += strArr[-i]
        resultStr += " "
    return resultStr

# Using two-pointer

def reverseString2(str):
    strArr = str.split(" ")
    i = 0
    j = len(strArr) - 1
    
    while i < j:
        strArr[i], strArr[j] = strArr[j], strArr[i]
        i += 1
        j -= 1
    resultStr = ""
    for x in strArr:
        resultStr += x
        resultStr += " "
    return resultStr
