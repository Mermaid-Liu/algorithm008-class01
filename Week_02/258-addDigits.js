/**
 * @param {number} num
 * @return {number}
 */
var addDigits = function(num) {
    if(num>9){
       num=num%9
        if(num==0){
            return 9
        }
    }
    return num
};
