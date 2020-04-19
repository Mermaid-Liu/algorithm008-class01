var twoSum = function(nums, target) {
    let res=[]
    let hashmap=new Map()
    nums.forEach(item=>{
        hashmap.set(item,1)
    })
    for(let item in nums){
        let temp=target-nums[item]
        nums.splice(item,1)
        if(hashmap.has(temp)){
            res.push(item)
        }
    }
    return res
};
