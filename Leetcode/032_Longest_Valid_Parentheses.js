/**
 * @param {string} 
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
// congratulation! you finish it on the first time



// another solution using stack
var longestValidParentheses_1 = function(s) {
    let stack = [], maxlen = 0, temp = 0;
    stack.push(-1);
    for (let i = 0; i < s.length; i++) {
    	if (s[i] === '(') {
    		stack.push(i);
    		console.log('push (', i);
    	} else if (s[i] === ')') {
    		stack.pop();
    		if (stack.length === 0) {
    			stack.push(i);
    			console.log('push )', i)
    		} else {
    			temp = i - stack[stack.length - 1]; 
    			maxlen = Math.max(maxlen, temp)
    			console.log('maxlen', maxlen, i)
    		}
    		
    	}

    }
    return maxlen;

}

// another solution o(n) & o(1)
var longestValidParentheses_2 = function(s) {
	let left = 0, right = 0, temp = 0, maxlen1 = 0, maxlen2 = 0;
	for (let i of s) {
		if (i === '(') {
			console.log('l to r, push (', i)
			left++;
		} else if (i === ')') {
			console.log('l to r, push )', i)
			right++;
			
		}
		if (left === right) {
			maxlen1 = Math.max(maxlen1, right*2);
			// stuppied !!!
			// left = right = 0;
			// flag = true;
			console.log('l', maxlen1)
		}else if (left < right) {
			left = right = 0;
			flag = false;
			console.log('break')
			
		}
	}
	// clear
	left = right = 0;
	for (var i = s.length - 1; i >= 0; i--) {
		if (s[i] === '(') {
			console.log('r to l, push (', i)
			left++;
		}else if (s[i] === ')') {
			console.log('r to l, push )', i)
			right++;
			
		}
		if (left === right) {
			maxlen2 = Math.max(maxlen2, left * 2);
			// left = right = 0;
			console.log('r', maxlen2)
		}else if (left > right) {
			console.log('break')
			left = right = 0;
		}
	}
	return Math.max(maxlen1, maxlen2);

	

}
console.log(longestValidParentheses_2(')()())'));



