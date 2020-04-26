/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if(s.length!=t.length){
        return false
    }
    let hashmap=new Map()
    for(let item of s){
        hashmap.has(item)?hashmap.set(item,hashmap.get(item)+1):hashmap.set(item,1)
    }
    for(let ch of t){
        if(hashmap.has(ch)&&hashmap.get(ch)>0){
            hashmap.set(ch,hashmap.get(ch)-1)
        }else{
            return false
        }
    }
    return true
};
