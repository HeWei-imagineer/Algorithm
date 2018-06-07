/**
 * @param {number[]} nums
 * @return {number}
 */
var firstMissingPositive = function(nums) {
	function* g() {
		let i = 1;
		while (true) {
			// statement
			yield i;
			i++;
		}
	}
    let s = new Set(nums);
    nums = [...s];
    /*nums.sort((x,y) => {
    	return x - y;
    });*/
    console.log(nums)
    nums.sort();
    console.log(s, nums);
    let gg = g();
    for (let i of nums) {
    	// let b;
    	if (i > 0){
    		let b = gg.next().value;
    		if (i !== b) {
    			return b;
    		}

    	}
    } 
    return gg.next().value;
};

console.log(firstMissingPositive([-1,4,2,1,9,10])) 
// console.log([-2,6,1,3,0,7,1,9,0].sort())