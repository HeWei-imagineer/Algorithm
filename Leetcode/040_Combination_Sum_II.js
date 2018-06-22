/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum2 = function(candidates, target) {
	let ans = new Set(), result = [];
	candidates.sort();
	findCircle_2(candidates, target, '', ans);
	// 处理结果，因为这里把结果存成了字符串，并利用set，去重复
	for (let i of ans) {
		result.push(i.split(',').map(item => {
			return parseInt(item)
			}).slice(1,));
	}
	// console.log(ans);
	console.log(result)
	return result;

};

let findCircle_2 = function(candidates, target, temp, ans) {
	// console.log(candidates, target, temp)
	if (target === 0) {
		return true;
	}
	if (target < 0 || candidates.length < 1) {
		return false;
	}

	if (findCircle_2(candidates.slice(1, ), target-candidates[0], temp + ',' + candidates[0], ans)) {
		ans.add(temp + ',' + candidates[0]);
	}
	if (findCircle_2(candidates.slice(1, ), target, temp, ans)) {
		ans.add(temp);
	}
}

combinationSum2([14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12],
27)