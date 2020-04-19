/**
 * @param {string} s
 * @return {character}
 */
var firstUniqChar = function(s) {
    if(s=='')return ' '
    let freq=new Array(26).fill(0)
    for(let i=0;i<s.length;i++){
        let index=s.charCodeAt(i)-"a".charCodeAt(0)
        freq[index]++
    }
    for(let i=0;i<s.length;i++){
        let index=s.charCodeAt(i)-"a".charCodeAt(0)
        if(freq[index]==1){
            return s.charAt(i)
        }
    }
    return ' '
};
