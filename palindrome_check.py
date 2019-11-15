# Palindrome check

# Solution 1:
def isPalindrome(string):
	return string == string[::-1]


# Solution 2;
def isPalindrome(string):
    reversed = []
    lst = [x for x in string]
    for i in range(len(lst) -1, -1, -1):
        reversed.append(lst[i])
    return reversed == lst
