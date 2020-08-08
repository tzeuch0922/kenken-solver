from Ken_Ken_Square import Ken_Ken_Square
class Ken_Ken_Block:
	
    # Instantiate Ken Ken block
    def __init__(self, value, operator):
        self.value = value
        self.operator = operator
        self.squares = []
    
    # Add square to list of squares in block
    def add_square(self, square):
        self.squares.append(square)
    
    # Set operator if originally unknown
    def set_operator(self, operator):
        if self.operator == '?':
            self.operator = operator
        else:
            print("Cannot change known operator.")
    
    # Get operator of block
    def get_operator(self):
        return self.operator
    
    # Get value of block
    def get_value(self):
        return self.value
        
    # Get squares in block
    def get_squares(self):
        return self.squares