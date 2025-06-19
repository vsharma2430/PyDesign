import ipywidgets as widgets
from IPython.display import display, HTML
from output.dark_theme import *
from copy import deepcopy

class ButtonBar:
    def __init__(self, item_dict=None, heading='', selector=None):
        self.item_dict = item_dict if item_dict is not None else {}
        self.heading = heading
        self.selector = selector
        self.container = None

    def set_heading(self, heading):
        """Set the heading of the ButtonBar."""
        grp = deepcopy(self)
        grp.heading = heading
        return grp
    
    def set_item_dict(self, item_dict):
        """Set the item dictionary of the ButtonBar."""
        grp = deepcopy(self)
        grp.item_dict = item_dict if item_dict is not None else {}
        return grp
        
    def add_item(self, key, item):
        """Add an item or list of items to a specific key in item_dict."""
        if key not in self.item_dict:
            self.item_dict[key] = []
        if isinstance(item, list):
            self.item_dict[key].extend(item)
        else:
            self.item_dict[key].append(item)
        # Refresh the button bar after adding items
        self.container = self.create_button_bar_for_dict()
        return self
        
    def set_selector(self, selector_func):
        """Set the selector function to be called when buttons are clicked."""
        self.selector = selector_func
        # Refresh the button bar to update button click handlers
        if self.item_dict:
            self.container = self.create_button_bar_for_dict()
        return self
            
    def create_button_bar_for_dict(self):
        """Create a button bar widget from the item dictionary."""
        # Set key prefix based on heading
        key_prefix = 'El.' if self.heading == 'Columns' else 'Tier' if self.heading in ['Tier Beams', 'Tier Int Beams'] else 'Level'
        
        # Create heading widget
        heading_widget = widgets.HTML(
            value=f'<h4 style="color: #ffffff; margin: 5px; font-weight: bold;">{self.heading}</h4>',
            layout=widgets.Layout(margin='5px')
        )
        
        # Create buttons for each key
        buttons = []
        for key in sorted(self.item_dict.keys()):
            button_label = f'{key_prefix} {key:.1f}' if isinstance(key, (int, float)) else f'{key_prefix} {key}'
            button = widgets.Button(
                description=button_label,
                tooltip=f'{self.heading} @ {key_prefix} {key}',
                layout=dark_layout
            )
            ids = self.item_dict[key] if isinstance(self.item_dict[key], list) else [self.item_dict[key]]
            
            def on_button_clicked(b, elevation=key, items=ids):
                if self.selector:
                    self.selector(items)
            
            if len(self.item_dict[key]) > 0:
                button.on_click(on_button_clicked)
                buttons.append(button)
        
        # Create button bar
        button_bar = widgets.HBox(buttons,
            layout=widgets.Layout(
                flex_flow='row wrap',
                padding='5px',
                background_color='#2d2d2d',
                border='1px solid #404040',
                border_radius='4px',
                margin='5px'
            ))
        
        # Combine heading and button bar
        container = widgets.VBox([heading_widget, button_bar], layout=widgets.Layout(
                padding='5px',
                background_color='#2d2d2d',
                border='1px solid #404040',
                border_radius='4px',
                margin='5px'
            ))
        
        self.container = container
        return container
    
    def display(self):
        """Display the button bar widget."""
        if self.container is None:
            self.container = self.create_button_bar_for_dict()
        display(self.container)