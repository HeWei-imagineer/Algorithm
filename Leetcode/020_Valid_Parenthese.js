/**
 * @param {string} s
 * @return {boolean}
 */
/*var isValid = function(s) {
	if(s.length<0){
		return true;
	}
	brackets = {
		'{':  1,
	    '}': -1,
		'(':  2,
		')': -2,
		'[':  3,
		']': -3
	};
	var arr = [];
	arr[-1] = '';
	for(var ch in s){
		if(brackets[s[ch]]>0){
			arr.push(brackets[s[ch]]);
		}else{
			if(arr.pop()+brackets[s[ch]]!=0){
				return false
			}
		}
	
	}
	if(arr.length===0){
		return true;
	}
	else{
		return false
	}
	
};
*/
//optimised
var isValid = function(s) {
	if(s.length<0){
		return true;
	}
	brackets = new Map([['{', '}'],['(', ')'],['[', ']']])
	stack = []
	for(var ch in s){
		if(brackets.has(s[ch])){
			stack.push(brackets[s[ch]]);
		}else{
			if(stack.pop()+brackets[s[ch]]!=0){
				return false
			}
		}
	
	}
	if(stack.length===0){
		return true;
	}
	else{
		return false
	}

};

console.log(isValid('{}[]')) 