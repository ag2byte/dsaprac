visited = [[]]


def exists(ar, word):
    # to get if word exists in an array or not
    rows = len(ar)
    col = len(ar[0])
    visited[[]*rows]*col
    count = 0
    for i in range(0, rows):
        for j in range(0, col):
            if ar[i][j] == word[0] and searchWord(i, j, 0, word, ar):
                count += 1

    print(count)


def searchWord(i, j, index, word, ar):
    if index == len(word):
        return True

    if visited[i][j] == True or ar[i][j] != word[index] or i < 0 or i >= len(ar) or j < 0 or j >= len(ar[i]):
        return False
    visited[i][j] = True

    if searchWord(i+1, j, index+1, word, ar) or searchWord(i-1, j, index+1, word, ar) or searchWord(i, j+1, index+1, word, ar) or searchWord(i, j-1, index+1, word, ar):

        return True
    visited[i][j] = False
    return False


def find():

    ar = ['pat', 'tac', 'ttt']
    word = 'cat'
    exists(ar, word)
