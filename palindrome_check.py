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


# Solution 3:
# Time complexity: O(n^2). In python, strings are immutable, each time we create a new string which take time.
# Space complexity: new strings creation
def isPalindrome(string):
    reversedString = ""
    for i in reversed(range(len(string))):
        reversedString += string[i]
    return string == reversedString
