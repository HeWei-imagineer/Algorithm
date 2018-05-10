/**
 * traverse nums from end to start as l, finding the first decreasing number i, 
 * then finding the l[j] just greater than i, swapping i and l[j], reversing l
 * @param {number[]} nums
 * @return {void} Do not return anything, modify nums in-place instead.
 */
var nextPermutation = function(nums) {
    let i = nums.length-1;
    // find the first decreasing number nums[i-1]
    for (i; i > 0; i--) {
        if (nums[i] > nums[i-1]) {
            break;
        }
    }
    // find l[j]
    console.log(i);
    if (i > 0) {
    	let j = nums.length - 1;
        for (j; j > i; j--) {
            if (nums[j] > nums[i-1]) {
            	break;
            }
        }
        console.log(j);
        let temp = nums[i-1];
        nums[i-1] = nums[j];
        nums[j] = temp;
        console.log(nums);
        nums.splice(i, nums.length-i, ...nums.slice(i).reverse());
    } else {
       // return the first permutation
        nums.reverse();
    }
};

let s = [5,4,3];
nextPermutation(s);
console.log(s);