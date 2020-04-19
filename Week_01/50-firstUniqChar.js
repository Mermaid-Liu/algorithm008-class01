/**
 * @param {string} s
 * @return {character}
 */
var firstUniqChar = function(s) {
    if(s=='')return ' '
    let hashObj={}
    for(let i=0;i<s.length;i++){
        if(hashObj[s[i]]==undefined){
            hashObj[s[i]]=1
        }else{
            hashObj[s[i]]=0
        }
    }
    for(let item in hashObj){
        if(hashObj[item]==1){
            return item
        }
    }
    return ' '
};
