from IPython.display import HTML
import ipywidgets as widgets

def create_html_widget_output(data):
    """
    Create HTML output for displaying data in an ipywidget with professional styling.
    
    Args:
        data (list): List of dictionaries containing id, name, type, and country
        
    Returns:
        str: HTML string ready for ipywidget display
    """
    
    # Start building the HTML with professional styling
    html = f"""
    <div style="background-color: #f8f9fa; border: 1px solid #dee2e6; border-radius: 8px; padding: 20px; margin-top: 10px; font-family: Arial, sans-serif;">
        <h3 style="color: #495057; margin-top: 0; margin-bottom: 15px; border-bottom: 2px solid #007bff; padding-bottom: 5px;">
            📊 Data Results ({len(data)} records)
        </h3>
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background-color: #007bff; color: white;">
                    <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6; font-weight: bold;">ID</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6; font-weight: bold;">Name</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6; font-weight: bold;">Type</th>
                    <th style="padding: 12px; text-align: left; border: 1px solid #dee2e6; font-weight: bold;">Country</th>
                </tr>
            </thead>
            <tbody>
    """
    
    # Add data rows with alternating background colors
    for i, item in enumerate(data):
        # Alternate row colors matching the steel widget design
        bg_color = "#e9ecef" if i % 2 == 0 else "#ffffff"
        
        html += f"""
                <tr style="background-color: {bg_color};">
                    <td style="padding: 10px; border: 1px solid #dee2e6;">
                        <span style="background-color: #28a745; color: white; padding: 2px 6px; border-radius: 8px; font-size: 11px; font-weight: bold;">
                            {item['id']}
                        </span>
                    </td>
                    <td style="padding: 10px; border: 1px solid #dee2e6; font-weight: bold; color: #007bff;">{item['name']}</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{item['type']}</td>
                    <td style="padding: 10px; border: 1px solid #dee2e6;">{item['country']}</td>
                </tr>
        """
    
    # Close the table and div
    html += """
            </tbody>
        </table>
    </div>
    """
    
    return html


# Example usage with your data
def display_data_widget(data):
    """
    Function to use with ipywidgets HTML widget
    """
    # Generate HTML
    html_content = create_html_widget_output(data)
    
    # Create and return the widget
    html_widget = widgets.HTML(value=html_content)
    
    return html_widget

# Alternative: Simple function that returns HTML string for direct use
def get_html_string(data):
    """
    Simple function that returns HTML string for your data
    Usage: 
        html_string = get_html_string(your_data)
        display(HTML(html_string))
    """
    return create_html_widget_output(data)
