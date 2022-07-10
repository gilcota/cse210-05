import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the cycle collides
    with other cycle's trail, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the cycle collides with one other cycle's trail
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        #cycle in the left - red one
        cycle = cast.get_first_actor("cycles")
        head = cycle.get_segments()[0]
        segments = cycle.get_segments()[1:]
        
        #cycle in the rigth - green one
        cycle1 = cast.get_second_actor("cycles")
        head1 = cycle1.get_segments()[0]
        segments1 = cycle1.get_segments()[1:]

        #checks collision of red cycle against green cycle's trail
        for segment in segments1:
            if head.get_position().equals(segment.get_position()):
                self._is_game_over = True
                cycle.set_game_over()
                cycle1.set_game_over()

        #checks collision of green cycle against red cycle's trail
        for segment in segments:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True
                cycle1.set_game_over()
                cycle.set_game_over()

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the cycles and trails white
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            cycle = cast.get_first_actor("cycles")
            cycle1 = cast.get_second_actor("cycles")

            segments = cycle.get_segments()
            segments1 = cycle1.get_segments()            

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for segment in segments:
                segment.set_color(constants.WHITE)  

            for segment in segments1:
                segment.set_color(constants.WHITE)