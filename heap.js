/**
 * package a kind of type to built heap
 * @class
 */

class heapNode{
	/**
	 * @param {object} ob: heap's element
	 * @param {string} val: the priority val, decide elements' order in heap
	 */
	constructor(ob,val){
		this.ob = ob;
		this.val = val;
	}
}


class Heap {
	constructor() {
		this.arr = [];
		// judge whether the param is reference or constant 
		if (arguments.length == 1) {
			for(let i of arguments[0]) {
			let heap = new heapNode(i,i);
			this.arr.push(heap);
			}
		} else if (arguments.length == 2) {
			for(let i of arguments[0]) {
			let heap = new heapNode(i,i[arguments[1]]);
			this.arr.push(heap);
			}
		}
		this.downToup();
	}

	downToup() {
		for (let i = Math.floor(this.arr.length/2-1);i>=0;i--) {
			let k = this.arr[(i+1)*2-1].val > this.arr[i].val ? (i+1)*2-1 : i; 

			if (this.arr.length > (i+1)*2) {
				k = this.arr[(i+1)*2].val > this.arr[k].val ? (i+1)*2 : k; 
			} 

			if (k !== i) {
				let temp = this.arr[i];
				this.arr[i] = this.arr[k];
				this.arr[k] = temp; 
			}
		}
	}

	upTodown(start) {
		for(let i = start;i<=Math.floor(this.arr.length/2-1);i++) {
			let k = this.arr[(i+1)*2-1].val > this.arr[i].val ? (i+1)*2-1 : i; 
		
			if (this.arr.length > (i+1)*2) {
				k = this.arr[(i+1)*2].val > this.arr[k].val ? (i+1)*2 : k; 
			} 

			if (k !== i) {
				let temp = this.arr[i];
				this.arr[i] = this.arr[k];
				this.arr[k] = temp; 
			}
		}
	}

	getTop() {
		return this.arr[0].ob;
	}

	add(ob,val=0) {
		let node;
		if(val === 0) {
			node = new heapNode(ob,ob);
		} else {
			node = new heapNode(ob,ob[val]);
		}
		this.arr.push(node);
		this.downToup();
	}

	delete() {
		this.arr[0] = this.arr[this.arr.length-1];
		this.arr.pop();
		this.upTodown(0);
	}

}

/**
 * a useful datastructure of nodeList
 * @class
 */
class Node {
	constructor(val=0) {
		this.val = val;
		this.next = none;
	}
}