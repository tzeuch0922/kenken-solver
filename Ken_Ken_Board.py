from Ken_Ken_Square import Ken_Ken_Square
from Ken_Ken_Block import Ken_Ken_Block

class Ken_Ken_Board:

	# Instantiate Board
	def __init__(self, squares, blocks):
		
        # Check to see if board is perfect square
        if len(squares) not in [pow(i, 2) for i in range(5, 10)]:
            print("Board length error:")
            print("Board should be perfect square")
            
        self.board = []
        self.blocks = []
        
        for val in squares:
            self.board.append(Ken_Ken_Square(val))
            
        for val in blocks:
            self.board.append(Ken_Ken_Block(*val))
            
    # Print Ken Ken Board
    def print_board(self):
        for i in range(0, 9):
            print('_______________________________________________________')
            for j in range(0, 3):
                if j == 0:
                    print('|5+   |8-   |90*        |7/                           |')
                elif j == 1:
                    print('|  3  |  7  |  9     5  |  8     1     2     4     6  |')
                else:
                    print('|     |     |     |     |     |     |     |     |     |')
        print('_______________________________________________________')
        
    # Get block value of square.
    def get_block_value(self, x, y):
        return self.block[self.get_block_number(x, y)].get_number()
        
    # Get block operator of square.
    def get_block_operator(self, x, y):
        return self.block[self.get_block_number(x, y)].get_operator()
    
    # Get square value of square.
    def get_square_value(self, x, y):
        index = (y * 9) + x
        return self.board[index].get_value()
        
    # Get block number of square.
    def get_block_number(self, x, y):
        index = (y * 9) + x
        return self.board[index].get_block_number()