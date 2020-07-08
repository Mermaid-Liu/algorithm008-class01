from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not beginWord or not endWord or not wordList:
            return 0
        dict=defaultdict(list)
        queue=[(beginWord,1)]
        visited={beginWord:True}
        l=len(beginWord)
        for word in wordList:
            for i in range(l):
                dict[word[:i]+'*'+word[i+1:]].append(word)
        
        while queue:
            cur,step=queue.pop(0)
            for i in range(l):
                new=cur[:i]+'*'+cur[i+1:]
                for word in dict[new]:
                    if word==endWord:
                        return step+1
                    if word not in visited:
                        visited[word]=True
                        queue.append((word,step+1))
                dict[new]=[]
        return 0
