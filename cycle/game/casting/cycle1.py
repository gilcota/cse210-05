import constants

from game.casting.actor import Actor
from game.shared.point import Point


class Cycle1(Actor):
    """
    A green cycle that leaves a trail behind
    
    The responsibility of Cycle is to move itself.

    Attributes:
        _points (int): The number of points the food is worth.
        _segments (Dict[string]): The segments drawn.
        _game_over (boolean): Whether or not the game is over.
    """
    def __init__(self):
        super().__init__()
        self._segments = []
        self._create_cycle()
        self._game_over = False

    def set_game_over(self):
        """Sets the game over flag if the cycle collides with one other cycle's trail"""
        self._game_over = True

    def get_segments(self):
        """Gets the segments"""        
        return self._segments

    def move_next(self):
        """Moves segments and adds to trail"""        
        # move all segments
        for segment in self._segments:
            segment.move_next()
        self.grow_trail(1)

        # update velocities
        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_cycle(self):
        """Gets the green cycle"""                
        return self._segments[0]

    def grow_trail(self, number_of_segments):
        """Leaves a trail where the cycle goes

        Args:
            number_of_segments (int): Amount of trails left per move
        """

        #leave trail behind                
        for i in range(number_of_segments):
            trail = self._segments[-1]
            velocity = trail.get_velocity()
            offset = velocity.reverse()
            position = trail.get_position().add(offset)
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")

            #while playing, trail is red; if game over, white
            if self._game_over == False:
                segment.set_color(constants.GREEN)
            else: 
                segment.set_color(constants.WHITE)
            
            self._segments.append(segment)

    def turn_cycle(self, velocity):
        """Turns cycle

        Args:
            number_of_segments (int): Amount of trails left per move
        """        
        self._segments[0].set_velocity(velocity)
    
    def _create_cycle(self):
        """Creates cycle, represented by an @ symbol"""

        x = int((constants.MAX_X / 6) * 5)
        y = int((constants.MAX_Y / 2))

        position = Point(x, y)
        velocity = Point(0, 0)            
        text = "@"
        color = constants.GREEN
        
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_text(text)
        segment.set_color(color)
        self._segments.append(segment)