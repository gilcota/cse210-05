import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the cycle.
    
    The responsibility of ControlActorsAction is to get the direction and move the cycle's cycle.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service

        #direction of red cycle
        self._direction = Point(0, -constants.CELL_SIZE)
        #direction of green cycle
        self._direction1 = Point(0, -constants.CELL_SIZE)        

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        """First Player - Red Cycle"""        
        # p1 left
        if self._keyboard_service.is_key_down('a'):
            self._direction = Point(-constants.CELL_SIZE, 0)
        
        # p1 right
        if self._keyboard_service.is_key_down('d'):
            self._direction = Point(constants.CELL_SIZE, 0)
        
        # p1 up
        if self._keyboard_service.is_key_down('w'):
            self._direction = Point(0, -constants.CELL_SIZE)
        
        # p1 down
        if self._keyboard_service.is_key_down('s'):
            self._direction = Point(0, constants.CELL_SIZE)
        
        cycle = cast.get_first_actor("cycles")
        cycle.turn_cycle(self._direction)


        """Second Player - Green Cycle"""
        # p2 left
        if self._keyboard_service.is_key_down('j'):
            self._direction1 = Point(-constants.CELL_SIZE, 0)
        
        # p2 right
        if self._keyboard_service.is_key_down('l'):
            self._direction1 = Point(constants.CELL_SIZE, 0)
        
        # p2up
        if self._keyboard_service.is_key_down('i'):
            self._direction1 = Point(0, -constants.CELL_SIZE)
        
        # p2down
        if self._keyboard_service.is_key_down('k'):
            self._direction1 = Point(0, constants.CELL_SIZE)
        
        cycle1 = cast.get_second_actor("cycles")
        cycle1.turn_cycle(self._direction1)        