var getHint = function(secret, guess) {
    let countA=0
    let countB=0
    let hashmap=new Map()
    let arr=[]

    for(let i=0;i<secret.length;i++){
        if(secret[i]==guess[i]){
            countA++
        }else{
            hashmap.has(secret[i])?hashmap.set(secret[i],hashmap.get(secret[i])+1):hashmap.set(secret[i],1)
            arr.push(guess[i])
        }
    }
    for(let i=0;i<arr.length;i++){
        if(hashmap.has(arr[i])){
            hashmap.get(arr[i])>1?hashmap.set(arr[i],hashmap.get(arr[i])-1):hashmap.delete(arr[i])
            countB++
        }
    }
    return countA+"A"+countB+"B"
};
