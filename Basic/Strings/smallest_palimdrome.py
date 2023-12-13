def checkPalimdrome(n):
    temp = n
    rev = 0
    while(n != 0):
        dig = n % 10
        rev = rev * 10 + dig
        n  = n // 10
    if(rev == temp):
        return True
    return False
def smallestPalimdrome(str):
    current_num = int(str) + 1
    while not checkPalimdrome(current_num):
        current_num += 1
    return current_num
    