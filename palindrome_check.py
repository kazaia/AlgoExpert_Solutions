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


# Solution 4:
# Time complexity: O(n) Instead of creating new strings each time, we use a list wich is ,unlike strings, mutable.
# Space complexity: O(n) as we creted a list of lenght n. 
def isPalindrome(string):
    reversedString = []
    for i in reversed(range(len(string))):
        reversedString.append(string[i])
    return string == "".join(reversedString)

# Solution 5: Recursive approach 







# Solution6: two pointers approach




