import ipywidgets as widgets

dark_theme_css = """
<style>
/* Global dark theme for widgets */
.widget-area {
    background-color: #1a1a1a !important;
    color: #ffffff !important;
}

.widget-box {
    background-color: #2d2d2d !important;
    border: 1px solid #404040 !important;
    border-radius: 4px !important;
}

.widget-label {
    color: #ffffff !important;
    font-weight: bold !important;
}

.widget-button {
    background-color: #404040 !important;
    color: #ffffff !important;
    border: 1px solid #606060 !important;
    border-radius: 3px !important;
}

.widget-button:hover {
    background-color: #505050 !important;
    border-color: #707070 !important;
}

.widget-button.selected {
    background-color: #0066cc !important;
    border-color: #0088ff !important;
}

.widget-text, .widget-textarea {
    background-color: #2d2d2d !important;
    color: #ffffff !important;
    border: 1px solid #404040 !important;
}

.widget-dropdown {
    background-color: #2d2d2d !important;
    color: #ffffff !important;
    border: 1px solid #404040 !important;
}
</style>
"""
# Display the CSS

dark_button_style = {
    'button_color': '#404040',
    'font_weight': 'bold'
}

dark_layout = widgets.Layout(
    border='1px solid #606060',
    margin='2px',
    padding='5px 10px',
    border_radius='3px',
    display='flex',
    justify_content='center',  # Centers content vertically in a flex container
    align_items='center',      # Ensures vertical alignment
    width='auto',
    height='auto',
)

dark_vbox = widgets.Layout(
    align_items='flex-start',
    padding='10px',
    background_color='#1a1a1a',  # Dark background
    border='2px solid #404040',
    border_radius='8px',
    margin='5px')