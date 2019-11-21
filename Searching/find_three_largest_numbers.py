# Find three largest numbers

# O(n) time 
# O(n) space

def findThreeLargestNumbers(array):
    output = []
    i = 0
    while i < 3:
        max_num = 0
        for item in array:
            if item > max_num:
                max_num = item
        output.append(max_num)
        array.remove(max_num)
        i += 1
    output.sort()
    return output

a = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
print(findThreeLargestNumbers(a))
