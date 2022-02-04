import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Collectors;
class Solution {
    int[] cols = new int[9];
    int[] rows = new int[9];
    int[] grids = new int[9];
    Map<Integer, Character> map = new HashMap<>() {{
        put(1 << 1, '1');
        put(1 << 2, '2');
        put(1 << 3, '3');
        put(1 << 4, '4');
        put(1 << 5, '5');
        put(1 << 6, '6');
        put(1 << 7, '7');
        put(1 << 8, '8');
        put(1 << 9, '9');
    }};

    public void solveSudoku(char[][] board) {
        int remaining = 81;
        for (int i = 0; i < 9; i++) {
            cols[i] = 1022;
            rows[i] = 1022;
            grids[i] = 1022;
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char cell = board[r][c];
                if (cell != '.') {
                    int mask = ~(1 << (cell - '0'));
                    cols[c] &= mask;
                    rows[r] &= mask;
                    int grid = getGrid(r, c);
                    grids[grid] &= mask;
                    remaining--;
                }
            }
        }

        boolean update;
        do {
            update = false;
            for (int r = 0; r < 9; r++) {
                for (int c = 0; c < 9; c++) {
                    char cell = board[r][c];
                    if (cell == '.') {
                        int possible = cols[c] & rows[r] & grids[getGrid(r, c)];
                        if (map.containsKey(possible)) {
                            cell = map.get(possible);
                            board[r][c] = cell;
                            int mask = ~possible;
                            cols[c] &= mask;
                            rows[r] &= mask;
                            int grid = getGrid(r, c);
                            grids[grid] &= mask;
                            remaining--;
                            update = true;
                        }
                    }
                }
            }
        } while (update);
        int[][] bitCounts = new int[9][9];
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                if (board[r][c] == '.') {
                    int bits = cols[c] & rows[r] & grids[getGrid(r, c)];
                    bitCounts[r][c] = Integer.bitCount(bits);
                }
            }
        }
        dfs(board, remaining, bitCounts);
        return;
    }

    boolean dfs(char[][] board, int remaining, int[][] bitCounts) {
        if (remaining == 0) {
            return true;
        }
        int bestR = 0;
        int bestC = 0;
        int minSelection = 10;
        outer:
        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                int bitCount = bitCounts[r][c];
                if (bitCount == 1) {
                    bestR = r;
                    bestC = c;
                    break outer;
                } else if (bitCount > 0 && bitCount < minSelection) {
                    bestR = r;
                    bestC = c;
                    minSelection = bitCount;
                }
            }
        }
        int bits = rows[bestR] & cols[bestC] & grids[getGrid(bestR, bestC)];
        for (int mask: map.keySet()) {
            if ((bits & mask) > 0) {
                char candidate = map.get(mask);
                board[bestR][bestC] = candidate;
                int grid = getGrid(bestR, bestC);
                cols[bestC] &= ~mask;
                rows[bestR] &= ~mask;
                grids[grid] &= ~mask;
                bitCounts[bestR][bestC] = 0;
                boolean valid = updateRows(bitCounts, bestC) && updateCols(bitCounts, bestR);
                if (valid) {
                    boolean result = dfs(board, remaining - 1, bitCounts);
                    if (result) {
                        return true;
                    }
                }
                // rollback
                cols[bestC] |= mask;
                rows[bestR] |= mask;
                grids[grid] |= mask;
                updateRows(bitCounts, bestC);
                updateCols(bitCounts, bestR);
                bitCounts[bestR][bestC] = Integer.bitCount(bits);
            }
        }
        return false;
    }

    int getGrid(int row, int col) {
        return (row / 3) * 3 + (col / 3);
    }

    boolean updateRows(int[][] bitCounts, int c) {
        for (int r = 0; r < 9; r++) {
            if (bitCounts[r][c] > 0) {
                int b = cols[c] & rows[r] & grids[getGrid(r, c)];
                int bc = Integer.bitCount(b);
                if (bc == 0) {
                    return false;
                }
                bitCounts[r][c] = bc;
            }
        }
        return true;
    }

    boolean updateCols(int[][] bitCounts, int r) {
        for (int c = 0; c < 9; c++) {
            if (bitCounts[r][c] > 0) {
                int b = cols[c] & rows[r] & grids[getGrid(r, c)];
                int bc = Integer.bitCount(b);
                if (bc == 0) {
                    return false;
                }
                bitCounts[r][c] = bc;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        Solution s = new Solution();
        char[][] board = new char[][] {
            {'.','.','9','7','4','8','.','.','.'},
            {'7','.','.','.','.','.','.','.','.'},
            {'.','2','.','1','.','9','.','.','.'},
            {'.','.','7','.','.','.','2','4','.'},
            {'.','6','4','.','1','.','5','9','.'},
            {'.','9','8','.','.','.','3','.','.'},
            {'.','.','.','8','.','3','.','2','.'},
            {'.','.','.','.','.','.','.','.','6'},
            {'.','.','.','2','7','5','9','.','.'}
        };
        s.solveSudoku(board);
        System.out.println(Arrays.stream(board).map(String::new).collect(Collectors.joining("\n")));
    }
}
