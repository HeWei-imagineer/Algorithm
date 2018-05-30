/**
 * @param {number} n
 * @return {string}
 */
var countAndSay = function(n) {
	// s当前序列， ss 数当前序列的序列
	let s = [1], ss = [1];
	for (let i = 0; i < n - 1; i++) {
		s = ss;
		// it's very important !!! if it losted, the j circulation will never stop
		ss = [];
		// console.log('i', i, s);
		let count = 1; 
		for (let j = 0; j < s.length; j++) {
			// console.log('j', j, count, 's.length', s.length);
			if (j < (s.length - 1) && s[j] === s[j+1]) {
				// console.log(count);
				count++;
			} else {
				// 数完相同的数字
				ss.push(count);
				ss.push(s[j]);
				count = 1;
				// console.log(ss);
			}
		}
	}
	console.log(ss.join(''));
    
};

countAndSay(4)