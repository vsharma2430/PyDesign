
import ipywidgets as widgets
from IPython.display import display, HTML
from output.dark_theme import *

def create_button_bar_for_dict(item_dict={}, heading='', selector=None):
    # Set key prefix based on heading
    key_prefix = 'El.' if heading == 'Columns' else 'Tier' if heading in ['Tier Beams', 'Tier Int Beams'] else 'Level'
    
    # Create heading widget
    heading_widget = widgets.HTML(
        value=f'<h4 style="color: #ffffff; margin: 5px 0; font-weight: bold;">{heading}</h4>',
        layout=widgets.Layout(margin='0px 0px 5px 0px')
    )
    
    # Create buttons for each key
    buttons = []
    for key in sorted(item_dict.keys()):
        button_label = f'{key_prefix} {key:.1f}' if isinstance(key, (int, float)) else f'{key_prefix} {key}'
        button = widgets.Button(
            description=button_label,
            tooltip=f'{heading} @ {key_prefix} {key}',
            layout=dark_layout
        )
        ids = item_dict[key] if isinstance(item_dict[key], list) else [item_dict[key]]
        
        def on_button_clicked(b, elevation=key, items=ids):
            if selector:
                selector(items)
        
        if(len(item_dict[key])>0):
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
            margin='0px 0px 10px 0px'
        ))
    
    # Combine heading and button bar
    container = widgets.VBox([heading_widget, button_bar], layout=widgets.Layout(
            padding='5px',
            background_color='#2d2d2d',
            border='1px solid #404040',
            border_radius='4px',
            margin='0px 0px 10px 0px'
        ))
    
    return container
