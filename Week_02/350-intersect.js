/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number[]}
 */
var intersect = function(nums1, nums2) {
 //排序+双指针法
    let i=0
    let j=0
    let res=[]
    nums1=nums1.sort((a,b)=>a-b)
    nums2=nums2.sort((a,b)=>a-b)
    while(i<nums1.length&&j<nums2.length){
        if(nums1[i]==nums2[j]){
            res.push(nums1[i])
            i++
            j++
        }else if(nums1[i]>nums2[j]){
            j++
        }else{
            i++
        }
    }
    return res
};
-------------------------------------------------------
var intersect = function(nums1, nums2) {
 //借助哈希表
    let hashmap=new Map()
    let res=[]
    for(let num1 of nums1){
        hashmap.has(num1)?hashmap.set(num1,hashmap.get(num1)+1):hashmap.set(num1,1)
    }
    for(let num2 of nums2){
        let hashkey=hashmap.get(num2)
        if(hashmap.has(num2)){
            res.push(num2)
        }
            hashmap.get(num2)>1?hashmap.set(num2,hashkey-1):hashmap.delete(num2)
    }
    return res
};
