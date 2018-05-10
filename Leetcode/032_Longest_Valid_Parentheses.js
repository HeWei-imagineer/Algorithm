/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
	let flag = 0;
	let ans = 0, count = 0;
	for (let i of s) {
		count++;
		if (i === '(') {
			flag += 1;
		} else {
			flag -= 1;
		}
		if (flag === 0 && count > ans) {
			ans = count;
		} else if (flag < 0) {
			count = 0;
		}

	}
	return ans;
};
console.log(longestValidParentheses('(()('));



