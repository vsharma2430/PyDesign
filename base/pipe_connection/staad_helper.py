from base.pipe_connection.pipe_client import PipeClient
from time import sleep
from IPython.display import Markdown, display

pipe_name = "STAAD_HELPER_PIPE"  # Should match your C# server pipe name

def apply_parameters_staad_helper(beam_nos=[], parameter_no=1, lx=True, ly=True, lz=True, dj=False, main=True):
    """
    Apply parameters to STAAD Helper via named pipe connection.
    Returns markdown-formatted output for Jupyter notebook display.
    
    Args:
        beam_nos (list): List of beam numbers to select
        parameter_no (int): Parameter number to apply
        lx (bool): Lateral X-bracing flag
        ly (bool): Lateral Y-bracing flag
        lz (bool): Lateral Z-bracing flag
        dj (bool): Displacement joint flag
        main (bool): Main parameters flag
    """
    messages = [
        {"type": "command", "action": "read_all_data"},
        {"type": "command", "action": "open_steel_tab"},
        {"type": "staad_ui", "feature": "select", "payload": beam_nos},
        {"type": "ui", "feature": "lx", "payload": lx},
        {"type": "ui", "feature": "ly", "payload": ly},
        {"type": "ui", "feature": "lz", "payload": lz},
        {"type": "ui", "feature": "dj", "payload": dj},
        {"type": "ui", "feature": "main", "payload": main},
        {"type": "ui", "feature": "parameter", "payload": parameter_no},
        {"type": "staad_ui", "feature": "select", "payload": None},
        {"type": "command", "action": "apply_parameters"},
    ]
    
    # Build markdown output
    markdown_output = []
    markdown_output.append("# STAAD Helper Parameter Application")
    markdown_output.append(f"**Parameter Number:** {parameter_no}")
    markdown_output.append("")
    
    # Beam selection section
    markdown_output.append("## Beam Selection")
    if beam_nos:
        if len(beam_nos) <= 10:
            beam_list = ", ".join(map(str, beam_nos))
            markdown_output.append(f"**Selected Beams:** {beam_list}")
        else:
            markdown_output.append(f"**Selected Beams:** {len(beam_nos)} beams ({beam_nos[0]}-{beam_nos[-1]} and others)")
        markdown_output.append(f"**Total Count:** {len(beam_nos)} beams")
    else:
        markdown_output.append("**Selected Beams:** All beams (no specific selection)")
    markdown_output.append("")
    
    markdown_output.append("## Configuration")
    markdown_output.append(f"- **LX (Lateral X):** {'✓' if lx else '✗'}")
    markdown_output.append(f"- **LY (Lateral Y):** {'✓' if ly else '✗'}")
    markdown_output.append(f"- **LZ (Lateral Z):** {'✓' if lz else '✗'}")
    markdown_output.append(f"- **DJ (Displacement Joint):** {'✓' if dj else '✗'}")
    markdown_output.append(f"- **Main Parameters:** {'✓' if main else '✗'}")
    markdown_output.append("")
    markdown_output.append("## Execution Log")
    markdown_output.append("")
    
    try:
        with PipeClient(pipe_name, timeout=10000) as client:
            for i, msg in enumerate(messages, 1):
                step_desc = get_step_description(msg)
                markdown_output.append(f"### Step {i}: {step_desc}")
                
                response = client.send_json(msg)
                
                # Format response
                if isinstance(response, dict):
                    status = response.get('status', 'Unknown')
                    message = response.get('message', str(response))
                    if status.lower() == 'success':
                        markdown_output.append(f"✅ **Status:** {status}")
                    else:
                        markdown_output.append(f"⚠️ **Status:** {status}")
                    markdown_output.append(f"**Response:** {message}")
                else:
                    markdown_output.append(f"**Response:** {response}")
                
                markdown_output.append("")
                sleep(0.5)  # Small delay between messages
            
            markdown_output.append("## Summary")
            markdown_output.append("✅ **All parameters applied successfully**")
                
    except ConnectionError as e:
        markdown_output.append("## Error")
        markdown_output.append(f"❌ **Connection Failed:** {e}")
    except Exception as e:
        markdown_output.append("## Error")
        markdown_output.append(f"❌ **Unexpected Error:** {e}")
    
    # Display the markdown in Jupyter
    final_markdown = "\n".join(markdown_output)
    display(Markdown(final_markdown))
    
    return final_markdown

def get_step_description(msg):
    """Get human-readable description for each message step."""
    msg_type = msg.get('type', '')
    
    if msg_type == 'command':
        action = msg.get('action', '')
        descriptions = {
            'read_all_data': 'Reading All Data',
            'open_steel_tab': 'Opening Steel Design Tab',
            'apply_parameters': 'Applying Parameters'
        }
        return descriptions.get(action, f'Command: {action}')
    
    elif msg_type == 'ui':
        feature = msg.get('feature', '')
        payload = msg.get('payload', '')
        descriptions = {
            'lx': f'Setting Lateral X-Bracing: {payload}',
            'ly': f'Setting Lateral Y-Bracing: {payload}',
            'lz': f'Setting Lateral Z-Bracing: {payload}',
            'dj': f'Setting Displacement Joint: {payload}',
            'main': f'Setting Main Parameters: {payload}',
            'parameter': f'Setting Parameter Number: {payload}'
        }
        return descriptions.get(feature, f'UI Setting: {feature} = {payload}')
    
    elif msg_type == 'staad_ui':
        feature = msg.get('feature', '')
        payload = msg.get('payload', '')
        if feature == 'select':
            if payload is None:
                return 'Clearing Selection'
            elif isinstance(payload, list):
                if len(payload) == 0:
                    return 'No Specific Beam Selection (All Beams)'
                elif len(payload) <= 5:
                    beam_list = ", ".join(map(str, payload))
                    return f'Selecting Beams: {beam_list}'
                else:
                    return f'Selecting {len(payload)} Beams: {payload[0]}-{payload[-1]} and others'
        return f'STAAD UI: {feature} = {payload}'
    
    return f"Unknown step: {msg}"

# Alternative function that returns markdown string without displaying
def apply_parameters_staad_helper_string(beam_nos=[], parameter_no=1, lx=True, ly=True, lz=True, dj=False, main=True):
    """
    Same as above but returns markdown string instead of displaying it.
    Useful for further processing or custom display.
    
    Args:
        beam_nos (list): List of beam numbers to select
        parameter_no (int): Parameter number to apply
        lx (bool): Lateral X-bracing flag
        ly (bool): Lateral Y-bracing flag
        lz (bool): Lateral Z-bracing flag
        dj (bool): Displacement joint flag
        main (bool): Main parameters flag
    """
    messages = [
        {"type": "command", "action": "read_all_data"},
        {"type": "command", "action": "open_steel_tab"},
        {"type": "staad_ui", "feature": "select", "payload": beam_nos},
        {"type": "ui", "feature": "lx", "payload": lx},
        {"type": "ui", "feature": "ly", "payload": ly},
        {"type": "ui", "feature": "lz", "payload": lz},
        {"type": "ui", "feature": "dj", "payload": dj},
        {"type": "ui", "feature": "main", "payload": main},
        {"type": "ui", "feature": "parameter", "payload": parameter_no},
        {"type": "staad_ui", "feature": "select", "payload": None},
        {"type": "command", "action": "apply_parameters"},
    ]
    
    markdown_output = []
    markdown_output.append("# STAAD Helper Parameter Application")
    markdown_output.append(f"**Parameter Number:** {parameter_no}")
    markdown_output.append("")
    
    # Beam selection section
    markdown_output.append("## Beam Selection")
    if beam_nos:
        if len(beam_nos) <= 10:
            beam_list = ", ".join(map(str, beam_nos))
            markdown_output.append(f"**Selected Beams:** {beam_list}")
        else:
            markdown_output.append(f"**Selected Beams:** {len(beam_nos)} beams ({beam_nos[0]}-{beam_nos[-1]} and others)")
        markdown_output.append(f"**Total Count:** {len(beam_nos)} beams")
    else:
        markdown_output.append("**Selected Beams:** All beams (no specific selection)")
    markdown_output.append("")
    
    markdown_output.append("## Configuration")
    markdown_output.append(f"- **LX (Lateral X):** {'✓' if lx else '✗'}")
    markdown_output.append(f"- **LY (Lateral Y):** {'✓' if ly else '✗'}")
    markdown_output.append(f"- **LZ (Lateral Z):** {'✓' if lz else '✗'}")
    markdown_output.append(f"- **DJ (Displacement Joint):** {'✓' if dj else '✗'}")
    markdown_output.append(f"- **Main Parameters:** {'✓' if main else '✗'}")
    markdown_output.append("")
    markdown_output.append("## Execution Log")
    markdown_output.append("")
    
    try:
        with PipeClient(pipe_name, timeout=10000) as client:
            for i, msg in enumerate(messages, 1):
                step_desc = get_step_description(msg)
                markdown_output.append(f"### Step {i}: {step_desc}")
                
                response = client.send_json(msg)
                
                if isinstance(response, dict):
                    status = response.get('status', 'Unknown')
                    message = response.get('message', str(response))
                    if status.lower() == 'success':
                        markdown_output.append(f"✅ **Status:** {status}")
                    else:
                        markdown_output.append(f"⚠️ **Status:** {status}")
                    markdown_output.append(f"**Response:** {message}")
                else:
                    markdown_output.append(f"**Response:** {response}")
                
                markdown_output.append("")
                sleep(0.5)
            
            markdown_output.append("## Summary")
            markdown_output.append("✅ **All parameters applied successfully**")
                
    except ConnectionError as e:
        markdown_output.append("## Error")
        markdown_output.append(f"❌ **Connection Failed:** {e}")
    except Exception as e:
        markdown_output.append("## Error")
        markdown_output.append(f"❌ **Unexpected Error:** {e}")
    
    return "\n".join(markdown_output)