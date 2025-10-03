class Queen:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.position = (row, column)
        self.position = self._check_validity()

    def _check_validity(self):
        row = self.row
        column = self.column
        if row > 7:
            raise ValueError ('row not on board')
        if column > 7:
            raise ValueError ('column not on board')
        if row < 0:
            raise ValueError ('row not positive')
        if column < 0:
            raise ValueError ('column not positive')
        
    def can_attack(self, another_queen):
        if (self.row == another_queen.row) and (self.column == another_queen.column):
            raise ValueError ('Invalid queen position: both queens in the same square')
        if self.row == another_queen.row:
            return True 
        if self.column == another_queen.column:
            return True
        if abs(self.row - another_queen.row) == abs(self.column - another_queen.column):
            return True
        else:
            return False
