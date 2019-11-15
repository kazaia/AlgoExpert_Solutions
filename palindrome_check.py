# Palindrome check

def isPalindrome(string):
    reversed = []
    lst = [x for x in string]
    for i in range(len(lst) -1, -1, -1):
        reversed.append(lst[i])
    return reversed == lst
