let treeMap = function(tree,f) {
	let temp = [];
	let queue = [];
	let count1 = 0;
	let count2 = 0; 
	if (arguments.length === 1) {
		return tree;
	} else if (typeof(arguments[1]) === 'function') {
		
		temp.unshift(tree[0]);
		while (temp.length !== 0) {
			count1++;
			let node = temp[0];
			console.log('temp',temp,'node',node.name)
			while (node.children !== undefined) {
				count2++;
				console.log('queue',queue)
				console.log('')
				while (temp.length !==0 && queue.length !== 0 && node.children.indexOf(queue[queue.length-1]) !== -1) {
				    console.log('children already visited',node.name)
					node = temp.shift();
					queue.push(node);
					node = temp[0];

				}
				if (temp.length === 0){
					return queue;
				}

				let i= node.children.length-1;
				for (i; i >= 0; i--) {
	 				temp.unshift(node.children[i]);
				}
				node = temp[0];
				console.log(node.name);
				if(count2>4)break;
			}
		console.log('remove')
		//queue.forEach(f); 
		node = temp.shift();
		queue.push(node);
		if(count1>1)break;
		}
		
	}

		return queue;
	
}

const tree = [
  {
    id: 1,
    name: '张三',
    children: [
    	{
    		id: 2,
    		name: '李四',
    		children: [
    			{
    				id: 5,
    				name: '张五'
    			}
    		]
    	}
    ]
  },
  {
    id: 6,
    name: '玛丽'
  }
]
console.log('ans',treeMap(tree,treeMap));