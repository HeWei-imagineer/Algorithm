/*/**
 * @param {string} s
 * @param {string[]} words
 * @return {number[]}
 */

var findSubstring = function(s, words) {
	if (!s) return [];
	if (words.length === 0) return [0];
	var ans = [];
	var index;
	var temp;
	var star = 0;
	var wordsLehgth = words.join('').length;
	do {
		// index = [s.indexOf(i) for (i of words)];
		// find the first position of each word in s
        index = words.map(function(elem) {
        	return s.indexOf(elem, star);
        });
        console.log(star);
        console.log('index', index);
        // why sort doesn't work
		temp = index.slice().sort((x,y) => x-y);
		// if every word can be find in s
		//temp's length always > 1, the last one needn't shift 
		while (temp.indexOf(-1)===-1 && temp.length>1) {
			console.log('temp',temp);
			console.log(index.indexOf(temp[0]));
			console.log(words[index.indexOf(temp[0])].length + temp[0]);

			// find position of another circle
			if (index.indexOf(words[index.indexOf(temp[0])].length + temp[0])!==-1) {
				temp.shift();
			} else {
				break;
			}
		}
		//hack
		if (temp.length===1) {
			ans.push(index.sort((x,y) => x-y)[0])
		} else {
			return ans;
		}
		// find the another star
		star = index[0]+wordsLehgth;
// more details
	} while (index.indexOf(-1) === -1 ); 

	return ans; 
};

console.log(findSubstring('barfoofoobarthefoobarman',['foo','bar',"the"]))

// dump

// optimize
// find index of each word in s and use priority queue store them
