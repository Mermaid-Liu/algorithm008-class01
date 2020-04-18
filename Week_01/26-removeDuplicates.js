var removeDuplicates = function(nums) {
   //双指针【把不同的字符移到最前面来】
   let p=0
   let q=1
   while(q<nums.length){
       if(nums[p]!=nums[q]){
           if(q-p>1){
            nums[p+1]=nums[q]
           }
           p++
       }
       q++
   }
   return p+1
};
