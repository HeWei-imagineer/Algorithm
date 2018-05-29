/**
 * @param {character[][]} board
 * @return {void} Do not return anything, modify board in-place instead.
 */
// your thought is so simple that can't solve the problems
/*var solveSudoku = function(board) {
    let rows = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
        sub_box = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
        columns = [[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9],[1,2,3,4,5,6,7,8,9]],
        blank = 0;
        for (let i = 0; i < board.length; i++) {
            for(let j = 0; j < board.length; j++){
                let c = board[i][j];
                let idx = Math.floor(i / 3) * 3 + Math.floor(j / 3); 
                if (c === '.') {
                    blank++;
                } else {
                	c = parseInt(c);
                	//console.log(c)
                	//console.log(rows[i].indexOf(c))
                    rows[i].splice(rows[i].indexOf(c), 1);
                    //console.log(rows[i])
                    columns[j].splice(columns[j].indexOf(c), 1);
                    sub_box[idx].splice(sub_box[idx].indexOf(c), 1);
                }
            }
            //console.log(rows[i])
        }

        console.log('row',rows, 'columns', columns, 'sub_box', sub_box)
        while (blank > 0) {
        	console.log('blank', blank)
        	console.log(board);
            // statement
            for (let i = 0; i < board.length; i++) {
                for(let j = 0; j < board.length; j++){
                	if (board[i][j] !== '.') {
                		continue;
                	}
                	let idx = Math.floor(i / 3) * 3 + Math.floor(j / 3);
                    let last = [rows[i], columns[j], sub_box[idx]].reduce(function(accumulator, currentValue) {
                    	return currentValue.filter(function(index) {
                    		return accumulator.indexOf(index) !== -1;
                    	});
                    })
                    //console.log(last)
                    if (last.length === 1) {
                    	board[i][j] = last[0].toString(); 
                    	blank--;
                    	let c = last[0];
                    	rows[i].splice(rows[i].indexOf(c), 1);
	                    columns[j].splice(columns[j].indexOf(c), 1);
	                    sub_box[idx].splice(sub_box[idx].indexOf(c), 1);
                    }
                }
        }
    }

};*/

var solveSudoku = function(board) {
	solve(board);
}
var solve = function(board) {

        for (let i = 0; i < board.length; i++) {
            for(let j = 0; j < board.length; j++){
                if (board[i][j] === '.') {
                	// it's the key point, every position contains the next posion's calculate
                	for (let c = 1; c <= board.length; c++) {
                		if (isValid(board, i, j, c)) {
                			//console.log(c)
                    		board[i][j] = c.toString();
                    		if (solve(board)) {
                    			return true;
	                    	} else {
	                    		board[i][j] = '.';
	                    	}
                    	} 
                	}
                	return false;
                }
            }
            //console.log(rows[i])
        }
        return true;
};


let isValid = function(board, i, j, c) {
	c = c.toString();
	//console.log(i, j, c)
	//c.toString(); the type of c changed. now it's string
	// the begin x index of sub_box
	let b_idx = Math.floor(i/3) * 3;
	// the begin y index of sub_box
	let b_idy = Math.floor(j/3) * 3;
	for (let k = 0; k < board.length; k++) {
		// console.log('i,k', i, k, 'k,j', k, j, '', b_idx + ((Math.floor(k/3))), b_idy + (k % 3))

		// eg: sub_box(0): 00, 01, 02 ...
		
	    //console.log(board[i][k], board[k][j], board[b_idx + (Math.floor(k/3))][b_idy + (k % 3)])
		
		if (board[i][k] === c || board[k][j] === c || board[b_idx + (Math.floor(k/3))][b_idy + (k % 3)] === c) {
			return false;
		}
    }
    //console.log('false')
    return true;
};


let test = [
["5","3",".",".","7",".",".",".","."],
["6",".",".","1","9","5",".",".","."],
[".","9","8",".",".",".",".","6","."],
["8",".",".",".","6",".",".",".","3"],
["4",".",".","8",".","3",".",".","1"],
["7",".",".",".","2",".",".",".","6"],
[".","6",".",".",".",".","2","8","."],
[".",".",".","4","1","9",".",".","5"],
[".",".",".",".","8",".",".","7","9"]];

let test1 = [
[".",".","9","7","4","8",".",".","."],
["7",".",".",".",".",".",".",".","."],
[".","2",".","1",".","9",".",".","."],
[".",".","7",".",".",".","2","4","."],
[".","6","4",".","1",".","5","9","."],
[".","9","8",".",".",".","3",".","."],
[".",".",".","8",".","3",".","2","."],
[".",".",".",".",".",".",".",".","6"],
[".",".",".","2","7","5","9",".","."]]
solve(test1);
//console.log(isValid(test1, 0, 1, 1));
console.log(test1);
