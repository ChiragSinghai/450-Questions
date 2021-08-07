class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        score = [0, 0, 0, 0, 0, 0, 0, 0]    # horizontal (3) ; vertical (3) ; diagonal (2)
        for t, (x, y) in enumerate(moves):
            v = 1 if t % 2 == 0 else -1     # determine whose turn it is (1 and -1 for players A and B, respectively)
            # determine the lines on which the i'th move falls
            score[x] += v                   # determine the horizontal line 
            score[y + 3] += v               # vertical
            score[-2] += v * (x == y)       # does it lay on l-to-r diagonal?
            score[-1] += v * (x + y == 2)   # does it lay on r-to-l diagonal?
        for i in score:
            if i == 3:
                return 'A'
            if i == -3:
                return 'B'

        return 'Pending' if n < 9 else 'Draw'
        '''
        winningMove=[[[0,0],[0,1],[0,2]],
                     [[0,0],[1,0],[2,0]],
                     [[1,0],[1,1],[1,2]],
                     [[2,0],[2,1],[2,2]],
                     [[0,1],[1,1],[2,1]],
                     [[0,2],[1,2],[2,2]],
                     [[0,0],[1,1],[2,2]],
                     [[0,2],[1,1],[2,0]]
                     ]
        
        
        for move in winningMove:
            check=all(item in moves[::2] for item in move)
            if check :
                return "A"
            check=all(item in moves[1::2] for item in move)
            if check:
                return "B"
        if len(moves)!=9:
            return "Pending"
        return "Draw"
        '''
