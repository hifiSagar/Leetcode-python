from collections import defaultdict

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return []

        parents = defaultdict(list)
        level = {beginWord}
        found = False

        while level and not found:
            nextLevel = set()
            wordSet -= level

            for word in level:
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":
                        newWord = word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                            parents[newWord].append(word)
                            nextLevel.add(newWord)
                            if newWord == endWord:
                                found = True

            level = nextLevel

        if not found:
            return []

        res = []

        def dfs(word, path):
            if word == beginWord:
                res.append(path[::-1])
                return
            for p in parents[word]:
                dfs(p, path + [p])

        dfs(endWord, [endWord])
        return res