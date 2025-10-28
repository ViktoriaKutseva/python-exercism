# Globals for the directions
# Change the values as you see fit
EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction = direction
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.coordinates = (x_pos, y_pos)
    def move(self, commands: str = ''):
        direction = self.direction
        x_pos = self.x_pos
        y_pos = self.y_pos
        for command in commands:
            if command == 'L':
                direction = (direction + 1) % 4
            elif command == 'R':
                direction = (direction - 1) % 4
            elif command == 'A':
                if direction == 0:
                    x_pos += 1
                if direction == 1:
                    y_pos += 1
                if direction == 2:
                    x_pos -= 1
                if direction == 3:
                    y_pos -= 1            
        self.direction = direction  
        self.coordinates = (x_pos, y_pos)        
