let nums = [1,2,3,4,2,3,4,2,4,5];
let target = 2;
let occur = 0;

for(let i = 0; i < nums.length; i++){
    if (target === nums[i]){
        occur += 1;
    }
}

console.log("Occurences:\n", occur);