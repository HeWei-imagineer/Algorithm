/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
	if (target >= nums[0]) {
		for (let i = 0; i < nums.length; i++) {
			if (target === nums[i]) {
				return i;
			} else if (i > 0 && nums[i] < nums[i-1]) {
				return -1;
			}
		}
		return -1;

	} else if (target <= nums[nums.length-1]) {
		// console.log('tail')
		for (var i = nums.length - 1; i >= 0; i--) {
			// console.log('i', i)
			if (target === nums[i]) {
				return i;
			} else if (i > 0 && nums[i] < nums[i-1]) {
				return -1;
			}
		}
		// console.log('break')
		return -1;
		
	} else {
		return -1;
	}
};

console.log(search([4,5,6,7,0,1,2], 0)) 