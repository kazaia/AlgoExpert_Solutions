# Move element to end 

def moveElementToEnd(array, toMove):
    # Write your code here.
    count = 0
    for item in array:
        if item == toMove:
            array.remove(item)
            count += 1
    for item in range(count):
        array.append(toMove)
    return array    

a = [2, 1, 2, 2, 2, 3, 4, 2]
print(moveElementToEnd(a, 2))


#Solution2: Swaping elements (Order of elements is not important)
# O(n) Time / O(1) Space
def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) -1

    while i < j:
        if array[i] != toMove:
            i += 1
        if i < j and array[j] == toMove:
            j -= 1
        if array[i] == toMove and array[j] != toMove:
            array[i], array[j] = array[j], array[i]
    return array   

 

