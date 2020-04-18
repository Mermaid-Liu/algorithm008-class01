/**
 * @param {string} S
 * @return {string}
 */
var reverseOnlyLetters = function(S) {
    let builder=[]
    let len=S.length
    let regexp=/[a-zA-Z]/g
    for(let i=len-1;i>=0;i--){
        let c=S.charAt(i)
        if(c.match(regexp)){
            builder.push(c)
        }
    }
    for(let j=0;j<len;j++){
        let c=S.charAt(j)
        if(!c.match(regexp)){
            builder.splice(j,0,c)
        }
    }
    return builder.join('')
};
