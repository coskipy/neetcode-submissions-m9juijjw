class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        minis = defaultdict(list)

        for i in range(9):
            for j in range(9):
                num = board[i][j]

                if num == '.':
                    continue
                
                mini_key = (j // 3, i // 3)
                if num in rows[i] or num in cols[j] or num in minis[mini_key]:
                    return False

                else:
                    rows[i].append(num)
                    cols[j].append(num)
                    minis[mini_key].append(num)

        return True


