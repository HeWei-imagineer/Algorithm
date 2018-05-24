/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var searchRange = function(nums, target) {
	let left = 0, right = nums.length, middle = Math.floor((left + right)/2);
	while (left <= right) {
		// statement
		if (target < nums[middle]) {
			right = middle - 1;
		} else if (target > nums[middle]) {
			left = middle + 1;
		} else {
			let start, end;
			start = end = middle;
			while (nums[start-1] === target) {
				// statement
				start--;
			}
			while (nums[end+1] === target) {
				// statement
				end++;
			}
			return [start, end];
		}
	}
	return [-1, -1];
};

// another solution, deep understand for binary search
/**
 * @param {number[]} nums
 * @param {number} target
 * @param {boolen} left [Is it to find the first num]
 * @return {number}
 */
var searchFirst = function(nums, target, left) {
	let lo = 0, hi = nums.length, middle = Math.floor((lo + hi)/2);
	// console.log(lo, hi, middle)
	while (lo < hi) {
		middle = Math.floor((lo + hi)/2);
		// statement
		if (target < nums[middle] || (left && target === nums[middle])) {
			hi = middle;
		} else {
			lo = middle + 1;

		}
	}
	// need to judge whether it is answer
	return lo;
}
var searchRange_1 = function(nums, target) {
	let left = searchFirst(nums, target, true);
	if (left === nums.length || nums[left] !== target) {
		return [-1, -1];
	} else {
		return [left, searchFirst(nums, target, false)-1];
	}
}

console.log(searchRange_1([1], 1))