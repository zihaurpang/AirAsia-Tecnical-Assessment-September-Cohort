wordList = ['apple', 'mango', 'apple', 'orange', 'orange', 'apple', 'guava', 'mango','mango']

def findWordsWithFrequency(N,wordList):
    wordList_set = set(wordList)
    print(list(filter(lambda x:wordList.count(x)==N, wordList_set)))
    
findWordsWithFrequency(3,wordList)
