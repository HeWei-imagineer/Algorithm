/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
var combinationSum = function(candidates, target) {
	let ans = [];
	findCircle(candidates, target, [], ans);
	console.log(ans);
	return ans;
    
};

let findCircle = function(candidates, target, temp, ans) {
	if (target === 0) {
		return true;
	}
	if (candidates.length > 0) {
		let addSum = [];
		for (let i = 0; target - candidates[0]*i >= 0; i++) {
			if (i > 0) {
				addSum.push(candidates[0]);
			}
			if (findCircle(candidates.slice(1,), target - candidates[0]*i, [...temp, ...addSum], ans)) {
				ans.push( [...temp, ...addSum]);
				console.log(ans[ans.length-1]);
			};
		}

	}
	return false;
}
// congraduation! once time ac, but I still use the old way~ 
combinationSum([2,3,5],8);