def generate_model_results_html(all_members, theme='dark', step=0.5):
    """
    Generate HTML output for model results with customizable theme.
    
    Parameters:
    -----------
    all_members : object
        Object containing results with the following structure:
        - results['failed']: number of failed members
        - results['failed_members']: list of tuples (member_id, ratio)
        - results['average']: average utilization ratio
        - results['deviation']: standard deviation
        - results['result']: dictionary of all member ratios
    
    theme : str, optional
        Theme for the HTML output ('light' or 'dark'). Default is 'dark'.
    
    step : float, optional
        Step size for grouping utilization ratios. Default is 0.5.
    
    Returns:
    --------
    str
        HTML formatted string ready for display
    """
    
    # Theme configurations
    themes = {
        'light': {
            'container_bg': '#f8f9fa',
            'container_border': '#dee2e6',
            'text_color': '#495057',
            'header_color': '#495057',
            'accent_color': '#007bff',
            'table_header_bg': '#e9ecef',
            'table_border': '#dee2e6',
            'table_row_bg': '#ffffff',
            'table_alt_row_bg': '#f8f9fa'
        },
        'dark': {
            'container_bg': '#1e1e1e',
            'container_border': '#444444',
            'text_color': '#ffffff',
            'header_color': '#ffffff',
            'accent_color': '#00bfff',
            'table_header_bg': '#333333',
            'table_border': '#555555',
            'table_row_bg': '#2a2a2a',
            'table_alt_row_bg': '#252525'
        }
    }
    
    # Get theme colors
    colors = themes.get(theme, themes['light'])
    
    # Start building HTML output
    html_output = f"""
<div style="background-color: {colors['container_bg']}; border: 1px solid {colors['container_border']}; border-radius: 8px; padding: 20px; margin-top: 10px; font-family: Arial, sans-serif; color: {colors['text_color']};">
    <h3 style="color: {colors['header_color']}; margin-top: 0; margin-bottom: 15px; border-bottom: 2px solid {colors['accent_color']}; padding-bottom: 5px; font-weight: bold;">
        📋 Model Result (Whole Structure)
    </h3>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 10px;">
        <tr style="background-color: {colors['table_header_bg']};">
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; min-width: 150px; color: {colors['text_color']};">Number of Failed Members</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; min-width: 250px; color: {colors['text_color']};">Failed Members</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; min-width: 150px; color: {colors['text_color']};">Average Utilization Ratio</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; min-width: 130px; color: {colors['text_color']};">Standard Deviation</th>
        </tr>
"""

    # Extract data from all_members.results
    num_failed = all_members.results['failed']
    failed_members = [x for (x, y) in all_members.results['failed_members']] or 'None'
    failed_members_str = ", ".join(str(x) for x in failed_members) if failed_members != 'None' else 'None'
    average = all_members.results['average']
    deviation = all_members.results['deviation']

    # Format failed members with proper word wrapping and theme-appropriate colors
    failed_member_color = '#ffcccc' if theme == 'dark' else '#d73a49'
    failed_members_formatted = f"<div style='max-width: 300px; overflow-wrap: break-word; word-wrap: break-word; white-space: normal; color: {failed_member_color}; font-weight: bold;'>{failed_members_str}</div>"

    # Add row to the main table with proper alignment
    html_output += f"""
        <tr style="background-color: {colors['table_row_bg']};">
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: right; color: {colors['text_color']}; font-weight: bold;">{num_failed}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left;">{failed_members_formatted}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: right; color: {colors['text_color']}; font-weight: bold;">{average:.4f}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: right; color: {colors['text_color']}; font-weight: bold;">{deviation:.4f}</td>
        </tr>
    </table>
"""

    # Add Failed Utilization Ratios by Groups table if there are failed members
    if all_members.results['failed_members']:
        # Group failed members by utilization ratio with a step of 0.5
        groups = {}
        for member_id, ratio in all_members.results['failed_members']:
            # Calculate group ID based on ratio (e.g., 0.0-0.5, 0.5-1.0, etc.)
            group_id = f"{int(ratio // step) * step:.2f}-{(int(ratio // step) + 1) * step:.2f}"
            if group_id not in groups:
                groups[group_id] = []
            groups[group_id].append(member_id)
        
        html_output += f"""
    <h3 style="color: {colors['header_color']}; margin-top: 25px; margin-bottom: 15px; border-bottom: 2px solid {colors['accent_color']}; padding-bottom: 5px; font-weight: bold;">
        📋 Failed Utilization Ratios by Groups
    </h3>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 10px;">
        <tr style="background-color: {colors['table_header_bg']};">
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Ratio Range</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Failed Member IDs</th>
        </tr>
"""
        # Add rows with alternating colors
        for i, (group_id, member_ids) in enumerate(sorted(groups.items())):  # Sort by group_id for consistent order
            row_bg = colors['table_row_bg'] if i % 2 == 0 else colors['table_alt_row_bg']
            members_str = ", ".join(str(mid) for mid in sorted(member_ids))  # Sort member IDs for consistency
            html_output += f"""
        <tr style="background-color: {row_bg};">
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left; color: {colors['text_color']}; font-weight: bold;">{group_id}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left; color: {colors['text_color']}; font-weight: bold;">{members_str}</td>
        </tr>
"""
        html_output += "    </table>"

    # Add All Utilization Ratios by Groups table
    model_ratios = {k: v for k, v in all_members.results['result'].items() if v != 0.0}
    if model_ratios:
        # Group all members by utilization ratio with the specified step
        all_groups = {}
        for member_id, ratio in model_ratios.items():
            group_id = f"{int(ratio // step) * step:.2f}-{(int(ratio // step) + 1) * step:.2f}"
            if group_id not in all_groups:
                all_groups[group_id] = []
            all_groups[group_id].append(member_id)
        
        html_output += f"""
    <h3 style="color: {colors['header_color']}; margin-top: 25px; margin-bottom: 15px; border-bottom: 2px solid {colors['accent_color']}; padding-bottom: 5px; font-weight: bold;">
        📋 All Utilization Ratios by Groups
    </h3>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 10px;">
        <tr style="background-color: {colors['table_header_bg']};">
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Ratio Range</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Member IDs</th>
        </tr>
"""
        # Add rows with alternating colors
        for i, (group_id, member_ids) in enumerate(sorted(all_groups.items())):  # Sort by group_id for consistent order
            row_bg = colors['table_row_bg'] if i % 2 == 0 else colors['table_alt_row_bg']
            members_str = ", ".join(str(mid) for mid in sorted(member_ids))  # Sort member IDs for consistency
            html_output += f"""
        <tr style="background-color: {row_bg};">
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left; color: {colors['text_color']}; font-weight: bold;">{group_id}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left; color: {colors['text_color']}; font-weight: bold;">{members_str}</td>
        </tr>
"""
        html_output += "    </table>"

    # Add Failed Utilization Ratios table if there are failed members
    if all_members.results['failed_members']:
        html_output += f"""
    <h3 style="color: {colors['header_color']}; margin-top: 25px; margin-bottom: 15px; border-bottom: 2px solid {colors['accent_color']}; padding-bottom: 5px; font-weight: bold;">
        📋 Failed Utilization Ratios
    </h3>
    <table style="width: 100%; border-collapse: collapse; margin-bottom: 10px;">
        <tr style="background-color: {colors['table_header_bg']};">
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Member ID</th>
            <th style="padding: 12px; border: 1px solid {colors['table_border']}; font-weight: bold; text-align: left; width: 50%; color: {colors['text_color']};">Utilization Ratio</th>
        </tr>
"""
        # Add rows with alternating colors
        for i, (member_id, ratio) in enumerate(all_members.results['failed_members']):
            row_bg = colors['table_row_bg'] if i % 2 == 0 else colors['table_alt_row_bg']
            ratio_color = '#ffaa00' if theme == 'dark' else '#e36209'
            html_output += f"""
        <tr style="background-color: {row_bg};">
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: left; color: {colors['text_color']}; font-weight: bold;">{member_id}</td>
            <td style="padding: 12px; border: 1px solid {colors['table_border']}; text-align: right; color: {ratio_color}; font-weight: bold;">{ratio:.4f}</td>
        </tr>
"""
        html_output += "    </table>"

    html_output += "</div>"
    return html_output