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
moveElementToEnd´
