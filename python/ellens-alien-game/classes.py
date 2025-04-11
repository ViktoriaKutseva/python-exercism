"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes
    ----------
    (class)total_aliens_created: int
    x_coordinate: int - Position on the x-axis.
    y_coordinate: int - Position on the y-axis.
    health: int - Number of health points.

    Methods
    -------
    hit(): Decrement Alien health by one point.
    is_alive(): Return a boolean for if Alien is alive (if health is > 0).
    teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
    collision_detection(other): Implementation TBD.
    """
    total_aliens_created = 0  
    def __init__(self, x_coordinate: int, y_coordinate: int):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        Alien.total_aliens_created += 1
        Alien.health = 3
      
    def hit(self):
        self.health = self.health - 1
        # return self.health
        # return 

    def is_alive(self):
        if self.health > 0:
            return True
        return False

    def teleport(self, x_coordinate, y_coordinate):
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate

    def collision_detection(self,other_object):
        pass

def new_aliens_collection(alien_start_positions):
    return [Alien(x_point, y_point) for x_point, y_point in alien_start_positions]

alien_start_positions = [(4, 7), (-1, 0)]
aliens = new_aliens_collection(alien_start_positions)

for alien in aliens:
    	print(alien.x_coordinate, alien.y_coordinate)
     
# alien = Alien(2,0)
# alien_2 = Alien(3,4)
# # alien_3 = Alien(4,2)

# print(Alien.total_aliens_created)  
# #TODO:  create the new_aliens_collection() function below to call your Alien class with a list of coordinates.