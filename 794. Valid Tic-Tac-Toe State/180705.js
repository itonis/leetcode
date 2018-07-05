/**
 * @param {string[]} board
 * @return {boolean}
 */
var validTicTacToe = function(board) {
    var diff = board.join('').split('').reduce(function(acc,block){block=="X"?acc++:block=="O"?acc--:acc=acc;return acc;},0);
    if (diff<0 || diff>1)   return false;
    if (diff == 1) {
        if (checkHLine(board, "O") || checkVLine(board, "O") || checkDiagLine(board, "O")) return false;
    } else {
        if (checkHLine(board, "X") || checkVLine(board, "X") || checkDiagLine(board, "X")) return false;
    }
    return true
};

function checkHLine (board, player) {
    for (let i=0; i<board.length; i++) {
        let hasLine = true;
        for (let j=0; j<board[0].length; j++) {
            hasLine = hasLine && board[i][j] == player;
        }
        if (hasLine) return true;
    }
    return false;
}

function checkVLine (board, player) {
    for (let i=0; i<board[0].length; i++) {
        let hasLine = true;
        for (let j=0; j<board.length; j++) {
            hasLine = hasLine && board[j][i] == player;
        }
        if (hasLine) return true;
    }
    return false;
}

function checkDiagLine (board, player) {
    let hasLine = true;
    for (let i=0; i<board.length; i++) {
        hasLine = hasLine && board[i][i] == player;
    }
    if (hasLine) return true;

    hasLine = true;
    for (let i=0; i<board.length; i++) {
        hasLine = hasLine && board[i][board.length-i-1] == player;
    }
    return hasLine;
}