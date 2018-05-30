// Fibonacci
let fibonacci_1 = function(n) {
	if (n === 0) {
		return 0;
	}
	if (n === 1) {
		return 1;
	}
	if (n === 2) {
		return 2;
	}
	if (n > 2) {
		return fibonacci_1(n-1) + fibonacci_1(n-2);
	}
}

let fibonacci_2 = function(n, map) {
	if (map.has(n)) {
		return map.get(n);
	}
	if (n === 0) {
		return 0;
	}
	if (n === 1) {
		return 1;
	}
	if (n === 2) {
		return 2;
	}
	if (n > 2) {
		let temp = fibonacci_1(n-1) + fibonacci_1(n-2);
		map.set(n, temp);
		return temp;
	}
}

let fibonacci_3 = function(n, map) {
	if (n === 0) {
		return 0;
	}
	if (n === 1) {
		return 1;
	}
	if (n === 2) {
		return 2;
	}
	let a = 1, b = 2, c;
	for (let i = 2; i < n; i++) {
		c = a + b;
		a = b;
		b = c;
	}
	return c;
	
}
// map = new Map();
// console.log(fibonacci_2(5, map));
console.log(fibonacci_3(5));