class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        i2c = defaultdict(set)
        for word in wordList:
            for i, c in enumerate(word):
                i2c[i].add(c)

        bq, eq = {beginWord}, {endWord}
        res = 0
        
        while bq:
            res += 1
            nbq = set()
            for word in bq:
                for i, c in enumerate(word):
                    for sub in i2c[i]:
                        new = word[:i] + sub + word[i + 1:]
                        if new in eq:
                            return res + 1
                        if new in wordList:
                            wordList.remove(new)
                            nbq.add(new)
            bq = nbq
            if len(bq) > len(eq):
                bq, eq = eq, bq
        return 0
