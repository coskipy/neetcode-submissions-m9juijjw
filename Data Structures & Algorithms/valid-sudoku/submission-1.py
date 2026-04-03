class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        minis = defaultdict(list)

        # Hash puzzle
        for i in range(0, len(board)):
            
            for j in range(0, len(board[i])):
                if board[i][j] != '.':
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])

                    mini_row = (i) // 3 + 1
                    mini_col = (j) // 3 + 1
                    mini = (mini_col - 1) * 3 + mini_row
                    minis[mini - 1].append(board[i][j])


        # Check rows
        for row in list(rows.values()):
            seen = []
            for num in row:
                if num in seen:
                    print(f'{num} in row {row} is a duplicated. Seen already {seen}')
                    return False
                else:
                    seen.append(num)

        # Check cols
        for col in list(cols.values()):
            seen = []
            for num in col:
                if num in seen:
                    print(f'{num} in col {col} is a duplicated. Seen already {seen}')
                    return False
                else:
                    seen.append(num)

        # Check minis
        for mini in list(minis.values()):
            seen = []
            for num in mini:
                if num in seen:
                    print(f'{num} in mini {mini} is a duplicated. Seen already {seen}')
                    return False
                else:
                    seen.append(num)


        return True


