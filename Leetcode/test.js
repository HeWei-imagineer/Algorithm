/*
let b = [[1,2,3], [1,5], [1,8]]
console.log(b.reduce(function(accumulator, currentValue) {
	//console.log(accumulator)
                    	return currentValue.filter(function(index) {
                    		return accumulator.indexOf(index) !== -1;
                    	});
                      }))

let a = [1,2,3,4];

console.log(a.filter(function(index) {
                    		return index > 2;
                    	}))
console.log(b)*/

require("google-closure-library");

goog.require("goog.structs.PriorityQueue");

let q = new goog.structs.PriorityQueue();

let a = [5,6], b = [1,3], c = [0,4];
q.insert(a.length, a);
q.insert(b.length, b);
q.insert(c.length, c);

c.pop();

console.log(q.peek())