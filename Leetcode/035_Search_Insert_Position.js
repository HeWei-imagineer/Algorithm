/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// binary search
var searchInsert = function(nums, target) {
	let lo = 0, hi = nums.length - 1, middle;
	// remember when to jump out the loop(lo<=hi) and hi/lo equal middle or middle+-1
	while (lo <= hi) {
		middle = Math.floor((lo+hi)/2);
		if (target < nums[middle]) {
			hi = middle - 1;
		} else if (target > nums[middle]) {
			lo = middle + 1;
		} else {
			return middle;
		}
	}
	return lo; 
    
};
console.log(searchInsert([1,3,5,6],2))