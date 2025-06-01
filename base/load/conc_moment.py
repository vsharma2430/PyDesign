from base.load.load import Load
from base.staad_base.load import MemberDirection

class ConcentratedMoment(Load):
    def __init__(self,direction : MemberDirection, moment_value: float = -1, d1_value: float = 0, d2_value: float = 0):
        """
        Initialize a ConcentratedLoad object representing a concentrated force on a beam member.
        
        Args:
            direction : The direction of the force (default: Y).
            force_value (float): The magnitude of the force (default: -1).
            d1_value (float): Distance or parameter 1 for load position (default: 0).
            d2_value (float): Distance or parameter 2 for load position (default: 0).
        """
        self.direction = direction
        self.force_value = moment_value
        self.d1_value = d1_value
        self.d2_value = d2_value