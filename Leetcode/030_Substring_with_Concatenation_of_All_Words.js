/**
 * judge whether the words can concat without interrupt
 *
 * @param {Map} container: {string} key: each word, {array} value: index of word reprent in s
 */
let find = function(container, words, index) {
	console.log(container, words, index);
	for (let i of words) {
		if (container.get(i).indexOf(index) !== -1) {
			// !important
			if(arguments.callee(container, words.slice(0,words.indexOf(i)).concat(words.slice(words.indexOf(i)+1)), index + i.length)) {
				return true;
			}
		}
	}
	if (words.length === 0) {
		return true;
	} else {
		return false;
	}

}

/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */
var findSubstring = function(s, words) {

	let container = new Map();
	let temp1, temp2 = [Number.MAX_VALUE];
	let ans = [];
	// @param {Map} container: {string} key: each word, {array} value: index of word reprent in s
	for (let i of words) {
		let start = 0;
		let index = [];
		while (start < s.length && s.indexOf(i, start) !== -1) {
			index[index.length] = s.indexOf(i, start);
			start = index[index.length-1] + 1;
		}
		container.set(i,index);
	}
	console.log(container);
	/**
	 * example:  findSubstring ("wordgoodgoodgoodbestword",["word","good","best","word"]);
	 * container { 'word' => [ 0, 20 ], 
	         	   'good' => [ 4, 8, 12 ], 
	         	   'best' => [ 16 ] }
	    from 0, traverse words, judge whether every word can concat without interrupt, next 0 is 4
	 */
	while (container.size !==0) {
		for (let [key, value] of container) {
			if (value.length === 0) {
				//container.delete(key); 
				return ans;
			}
			console.log(key, value, temp2);
			if (value[0] < temp2[0]) {
				temp1 = key;
				temp2 = value;
			}
		}
		console.log('find index', temp1, temp2);
		let index = temp2[0] + temp1.length;
		// !important
		if (find(container, words.slice(0,words.indexOf(temp1)).concat(words.slice(words.indexOf(temp1)+1)), index)) {
			console.log(temp2)
			ans[ans.length] = temp2[0];
		}
		temp2.shift();
		console.log('container',container)
		console.log(container)
	}

	return ans;
}


let a = findSubstring ("wordgoodgoodgoodbestword",["word","good","best","word"]);
/*let container = new Map();
container.set('fo',[0,9]);
container.set('bar',[2,6]);
container.set('o',[1,5,10,11]);
let a = find(container, ['bar','o'], 2)*/
console.log(a);


