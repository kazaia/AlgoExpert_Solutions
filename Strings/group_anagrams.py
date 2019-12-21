# Group anagrams 


# Time complexity: O(wnlog(w)), whre n is the lenght of the words and n is the lenght of the array
# Space complexity: O(wn), whre n is the lenght of the words and n is the lenght of the array

def groupAnagrams(words):
    anagrams = {}
    sortedWords = []
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord in anagrams:
            anagrams[sortedWord].append(word)
        else:
            anagrams[sortedWord] = [word]
        
    return list(anagrams.values())



