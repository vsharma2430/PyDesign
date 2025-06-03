from copy import deepcopy

class WindLoad:
    def __init__(self, start_ele: float = 0, end_ele: float = 10, windward: float = 0, leeward: float = 0):
        self.start_ele = start_ele
        self.end_ele = end_ele
        self.windward = windward
        self.leeward = leeward
    
    def add_elevation(self, elevation: float) -> None:
        """
        Adds the specified elevation to both start and end elevations.
        
        Args:
            elevation (float): The elevation value to add to both start_ele and end_ele.
        """
        load = deepcopy(self)
        self.start_ele += elevation
        self.end_ele += elevation
        return load
    
add_elevation_to_wind_load_list_fn = lambda ground_level : lambda loads : list(map(lambda load: load.add_elevation(ground_level), [*loads]))