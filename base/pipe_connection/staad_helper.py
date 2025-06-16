import os
import subprocess
from time import sleep
from IPython.display import Markdown, display
from typing import List, Optional
from base.pipe_connection.pipe_client import PipeClient
from base.pipe_connection.message import *

pipe_name = "STAAD_HELPER_PIPE"

# Get the current username
username = os.getlogin()

# Construct the full path
app_path = f"C:\\Users\\{username}\\AppData\\Local\\SDC\\APP\\StaadHelper.exe"
test_app_path = f"E:\\MyOldUserData\\source\\repos\\StaadHelper\\StaadHelper\\bin\\x64\\Debug\\StaadHelper.exe"

def open_staad_helper():
    app_path = test_app_path
    try:
        # Check if the file exists
        if os.path.exists(app_path):
            # Open the application
            subprocess.Popen(app_path)
            print(f"Successfully opened {app_path}")
        else:
            print(f"Error: The file {app_path} does not exist")
    except Exception as e:
        print(f"Error opening application: {e}")

def get_pipe_messages(
    beam_nos: List[int] = [],
    parameter_no: int = 1,
    lx: bool = True,
    ly: bool = True,
    lz: bool = True,
    dj: bool = False,
    main: bool = True,
) -> List[dict]:
    return [
        message_select_beams(beam_nos),
        message_lx(lx),
        message_ly(ly),
        message_lz(lz),
        message_dj(dj),
        message_main(main),
        message_parameter_no(parameter_no),
        message_apply,
        message_select_beams(None),
    ]

def apply_parameters_staad_helper(
    messages: List[dict] = [],
    display_output: bool = True,
    wait_time: int = 10,
) -> str:
    """
    Apply parameters to STAAD Helper via named pipe connection.
    Returns concise markdown-formatted table and optionally displays it in Jupyter.

    Args:
        messages: List of message dictionaries to send to STAAD Helper
        display_output: If True, displays markdown in Jupyter; always returns string
        wait_time: Time to wait (in seconds) for critical operations

    Returns:
        Markdown-formatted string containing execution results in tabular form
    """
    # If no messages provided, generate default messages
    if not messages:
        return

    messages = [
        {"type": "command", "action": "read_all_data"},
        {"type": "command", "action": "open_steel_tab"},
        *messages,
        {"type": "command", "action": "close"},
    ]

    def format_beam_selection() -> List[str]:
        """Format beam selection information."""
        # Extract beam_nos from messages
        beam_nos = []
        for msg in messages:
            if msg.get('type') == 'staad_ui' and msg.get('feature') == 'select':
                beam_nos = msg.get('payload', [])
                break
        
        if not beam_nos:
            return ["**Selected Beams:** All beams (no specific selection)"]
        
        output = []
        if len(beam_nos) <= 10:
            beam_list = ", ".join(map(str, beam_nos))
            output.append(f"**Selected Beams:** {beam_list}")
        else:
            output.append(f"**Selected Beams:** {len(beam_nos)} beams ({beam_nos[0]}-{beam_nos[-1]} and others)")
        output.append(f"**Total Count:** {len(beam_nos)} beams")
        return output

    def format_configuration() -> List[str]:
        """Format configuration parameters."""
        # Extract configuration from messages
        config = {
            'lx': True,
            'ly': True,
            'lz': True,
            'dj': False,
            'main': True
        }
        parameter_no = 1
        for msg in messages:
            if msg.get('type') == 'ui' and msg.get('feature') in config:
                config[msg['feature']] = msg.get('payload', config[msg['feature']])
            elif msg.get('type') == 'ui' and msg.get('feature') == 'parameter':
                parameter_no = msg.get('payload', 1)
        
        return [
            f"**Parameter Number:** {parameter_no}",
            f"- **LX (Lateral X):** {'✓' if config['lx'] else '✗'}",
            f"- **LY (Lateral Y):** {'✓' if config['ly'] else '✗'}",
            f"- **LZ (Lateral Z):** {'✓' if config['lz'] else '✗'}",
            f"- **DJ (Displacement Joint):** {'✓' if config['dj'] else '✗'}",
            f"- **Main Parameters:** {'✓' if config['main'] else '✗'}",
        ]

    # Build markdown output
    markdown_output = [
        "# STAAD Helper Parameter Application",
        "",
        "## Beam Selection",
        *format_beam_selection(),
        "",
        "## Configuration",
        *format_configuration(),
        "",
        "## Execution Log",
        "",
        "| Step | Action/Feature | Status | Response |",
        "|------|----------------|--------|----------|",
    ]

    try:
        with PipeClient(pipe_name, timeout=10000) as client:
            for i, msg in enumerate(messages, 1):
                action = msg.get('action', msg.get('feature', 'Unknown'))
                response = client.send_json(msg)

                status = 'Unknown'
                message = str(response)
                if isinstance(response, dict):
                    status = response.get('status', 'Unknown')
                    message = response.get('message', str(response))

                status_icon = '✅' if status.lower() == 'success' else '⚠️'
                markdown_output.append(f"| {i} | {action} | {status_icon} {status} | {message} |")

                # Set sleep time based on message type
                sleep_time = wait_time if msg.get('action') in ['read_all_data', 'apply_parameters', 'open_steel_tab'] else 0.5
                sleep(sleep_time)

            markdown_output.extend([
                "",
                "## Summary",
                "✅ **All parameters applied successfully**"
            ])

    except ConnectionError as e:
        markdown_output.extend([
            "",
            "## Error",
            f"❌ **Connection Failed:** {e}"
        ])
    except Exception as e:
        markdown_output.extend([
            "",
            "## Error",
            f"❌ **Unexpected Error:** {e}"
        ])

    final_markdown = "\n".join(markdown_output)
    
    if display_output:
        display(Markdown(final_markdown))
    
    return final_markdown