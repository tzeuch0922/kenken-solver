class Ken_Ken_Square:

    # Instantiate square
    def __init__(self, block_number):
        self.value = 0
        self.block = block_number
        self.possible_values = []
        
    # Initialize possible_values based on dimensions of board
    def init_possible_values(max_value):
        self.possible_values = list(range(1, max+1))
        
    # Set value and replace possible_values
    def set_value(self, num):
        self.value = value
        self.possible_values.clear()
        self.possible_values.append(num)
        
    # Remove value from possible_values list and set value if only one possible value
    def remove_possible_value(self, num):
        self.possible_values.remove(num)
        if len(self.possible_values) == 1:
            self.set_value(self.possible_values[0])
            return True
        return False
        
    # get value of square
    def get_value(self):
        return self.value
        
    # get possible_values of square
    def get_possible_values(self):
        return self.possible_values