from IPython.display import HTML
import ipywidgets as widgets

def create_profile_widget(data, theme='dark', title=None, icon='📊'):
    """
    Create HTML widget for displaying data with professional styling and theme support.
    
    Args:
        data (list): List of dictionaries containing data
        theme (str): Theme ('light' or 'dark'). Default: 'dark'
        title (str): Custom title (optional)
        icon (str): Title icon. Default: '📊'
        
    Returns:
        widgets.HTML: HTML widget for display
    """
    themes = {
        'light': {
            'bg': '#f8f9fa', 'border': '#dee2e6', 'text': '#495057', 'header': '#495057',
            'accent': '#007bff', 'table_head_bg': '#007bff', 'table_head_text': '#ffffff',
            'table_border': '#dee2e6', 'row_bg': '#ffffff', 'alt_row_bg': '#e9ecef',
            'id_bg': '#28a745', 'id_text': '#ffffff', 'name': '#007bff', 'data': '#495057'
        },
        'dark': {
            'bg': '#1e1e1e', 'border': '#444444', 'text': '#ffffff', 'header': '#ffffff',
            'accent': '#00bfff', 'table_head_bg': '#0066cc', 'table_head_text': '#ffffff',
            'table_border': '#555555', 'row_bg': '#2a2a2a', 'alt_row_bg': '#252525',
            'id_bg': '#28a745', 'id_text': '#ffffff', 'name': '#00bfff', 'data': '#ffffff'
        }
    }
    
    colors = themes.get(theme, themes['light'])
    title = title or f"STAAD Profiles ({len(data)} records)"
    
    if not data:
        html = f"<div style='padding: 20px; text-align: center; color: {colors['text']};'>No data available</div>"
        return widgets.HTML(value=html)
    
    columns = list(data[0].keys())
    html = f"""
    <div style="background: {colors['bg']}; border: 1px solid {colors['border']}; border-radius: 8px; padding: 20px; margin-top: 10px; font-family: Arial, sans-serif; color: {colors['text']};">
        <h3 style="color: {colors['header']}; margin: 0 0 15px; border-bottom: 2px solid {colors['accent']}; padding-bottom: 5px; font-weight: bold;">
            {icon} {title}
        </h3>
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="background: {colors['table_head_bg']}; color: {colors['table_head_text']};">
                    {''.join(f'<th style="padding: 12px; text-align: left; border: 1px solid {colors['table_border']}; font-weight: bold;">{col.title()}</th>' for col in columns)}
                </tr>
            </thead>
            <tbody>
    """
    
    for i, item in enumerate(data):
        bg = colors['row_bg'] if i % 2 == 0 else colors['alt_row_bg']
        html += f'<tr style="background: {bg};">'
        for j, col in enumerate(columns):
            value = item.get(col, '')
            style = f"padding: 10px; border: 1px solid {colors['table_border']};"
            if j == 0:
                html += f'<td style="{style}"><span style="background: {colors['id_bg']}; color: {colors['id_text']}; padding: 2px 6px; border-radius: 8px; font-size: 11px; font-weight: bold;">{value}</span></td>'
            elif j == 1:
                html += f'<td style="{style} font-weight: bold; color: {colors['name']};">{value}</td>'
            else:
                html += f'<td style="{style} color: {colors['data']}; font-weight: bold;">{value}</td>'
        html += '</tr>'
    
    html += """
            </tbody>
        </table>
    </div>
    """
    
    return widgets.HTML(value=html)