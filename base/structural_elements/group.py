class BeamGroup:
    def __init__(self, heading='', item_dict=None):
        self.heading = heading
        self.item_dict = item_dict if item_dict is not None else {}
    
    def set_heading(self, new_heading):
        """Change the heading of the BeamGroup."""
        self.heading = new_heading
    
    def add_item(self, key, value):
        """Add a key-value pair to the item_dict."""
        self.item_dict[key] = value
    
    def update_items(self, new_dict):
        """Update item_dict with another dictionary."""
        if not isinstance(new_dict, dict):
            raise TypeError("Input must be a dictionary")
        self.item_dict.update(new_dict)