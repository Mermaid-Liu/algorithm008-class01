class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        countA=0
        countB=0
        dic1={}
        arr=[]
        siz=len(secret)
        for i in range(siz):
            if secret[i]==guess[i]:
                    countA+=1
            else:
                if secret[i] in dic1:
                    dic1[secret[i]]+=1
                else:
                    dic1[secret[i]]=1
                    arr.append(guess[i])
        for i in range(len(arr)):
            if arr[i] in dic1:
                if dic1[arr[i]]>1:
                    dic1[arr[i]]-=1
                else:
                    dic1.pop(arr[i])
                countB+=1
        return str(countA)+"A"+str(countB)+"B"
