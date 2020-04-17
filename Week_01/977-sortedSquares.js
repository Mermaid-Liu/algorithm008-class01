var sortedSquares = function(A) {
    let l=0
    let r=A.length-1
    let i=r
    let res=[]
    while(i>=0){
        let lft=A[l]*A[l]
        let rght=A[r]*A[r]
        if(lft>rght){
            res[i]=lft
            l++
        }else{
            res[i]=rght
            r--
        }
        i--
    }
    return res
};
