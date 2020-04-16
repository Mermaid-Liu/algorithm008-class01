var subtractProductAndSum = function(n) {
    let add=0; 
    let mul=1;
    while(n>0){
       let digit=n%10;
       n=Math.floor(n/10)
       add+=digit
       mul*=digit
    }
    return mul-add
};
