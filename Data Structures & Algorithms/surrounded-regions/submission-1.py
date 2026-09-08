class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols= len(board), len(board[0])
        ##1 : Capture unsurround regions O => T (sau đó dùng dfs để biến tất cả những O đang connect với T đó cũng thành T để khi có bảng kết cả cả vùng đó vẫn giữ nguyên )
        ##2 : duyệt cả grid biến các vùng surrounded O thành X 
        ##3: Biến toàn bộ T thành O lại

        def dfs(r,c):
            if( r<0 or c<0 or
                r>=rows or c>=cols or
                board[r][c]!= "O"):
                return
            board[r][c]= "T"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(rows):
            for c in range(cols):
                if (board [r][c]== "O" 
                    and (r in [0,rows-1] or c in[0,cols-1])):
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if board [r][c]== "O":
                    board[r][c]= "X"
        
        for r in range(rows):
            for c in range(cols):
                if board [r][c]== "T":
                    board[r][c]= "O"
                



        