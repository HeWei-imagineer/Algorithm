/**
 * @param {string} s
 * @return {number}
 */
var longestValidParentheses = function(s) {
	// dp: record the length of valid substring; max: the longest length of valid substring
	let dp = [], maxlen = 0;
	for (let i = 0; i < s.length; i++) {
		if (s[i] === '(') {
			console.log(i, s[i])
			dp[i] = 0;
		} else if (s[i] === ')' && i > 0 && s[i-1] === '(') {
			console.log(i, s[i], ')(')
			dp[i] = i > 1 ? dp[i - 2] + 2 : 2
		} else if (s[i] === ')' && i > 0 && s[i-1] === ')') {
			console.log(i, s[i], '))')
			if ((i - dp[i-1]-1) >= 0 && s[i - dp[i-1]-1] === '(') {
				dp[i] = (i-dp[i-1]-2) >=0 ? dp[i-1] + 2 + dp[i-dp[i-1]-2] : dp[i-1] + 2
			} else {
				dp[i] = 0;
			}
			
		} else {
			console.log(i, s[i], '0')
			dp[i] = 0
		}
		maxlen = Math.max(dp[i], maxlen);
	}
	console.log(dp)
	return maxlen;
};
console.log(longestValidParentheses('(()(()))(()))))('));



