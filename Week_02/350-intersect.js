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
