/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
	for (let i = 0; i < board.length; i++) {
		let set1 = new Set();
		for(let j = 0; j < board.length; j++){
			if (board[j][i] > -1) {
				if (set1.has(board[j][i])) {
					console.log('y')
					return false;
				} else {
					set1.add(board[j][i]);
				}
			}

		// for sub-box
			if (i % 3 === 0 && j % 3 === 0) {
				let k = 0, s = [];
				while (k < 3) {
					// statement
					let temp = board[i + k].slice(j, j + 3).filter( x => {
															return x > -1;
														});
					s[k] = new Set(temp);
					console.log(temp, s[k].size)
					if (temp.length !== s[k].size) {
						console.log('x1', i, j)
						return false;
					}
					k++;
				}
				let check = new Set([...s[0], ...s[1], ...s[2]]);
				if (check.size !== s[0].size + s[1].size + s[2].size) {
					console.log('y1')
					return false;
				}

			}
		}
		let temp = board[i].filter(x => {
			return x > -1;
		});
		let set2 = new Set(temp);
		if (temp.length !== set2.size) {
			console.log('y')
			return false;
		}
		
	}
	return true;
};


// another simple abstract
/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku_1 = function(board) {
	let rows = [{},{},{},{},{},{},{},{},{}],
		sub_box = [{},{},{},{},{},{},{},{},{}],
	    columns = [{},{},{},{},{},{},{},{},{}];
	for (let i = 0; i < board.length; i++) {
		for(let j = 0; j < board.length; j++){
			let c = board[i][j];
			if (c === '.') {
				continue;
			}
			let boxIndex = Math.floor(i/3)*3 + Math.floor(j/3);
			if (rows[i][c] == null && columns[j][c] == null && sub_box[boxIndex][c] == null) {
				rows[i][c] = '';
				columns[j][c] = '';
				sub_box[boxIndex][c] = '';
			} else {
				return false;
			} 
		}
	}
	return true;
}


console.log(isValidSudoku_1([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))