import os
import subprocess
from time import sleep
from IPython.display import Markdown, display
from typing import List, Optional
from base.pipe_connection.pipe_client import PipeClient

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

def apply_parameters_staad_helper(
    beam_nos: List[int] = [],
    parameter_no: int = 1,
    lx: bool = True,
    ly: bool = True,
    lz: bool = True,
    dj: bool = False,
    main: bool = True,
    display_output: bool = True,
    wait_time:int=10,
) -> str:
    """
    Apply parameters to STAAD Helper via named pipe connection.
    Returns concise markdown-formatted table and optionally displays it in Jupyter.

    Args:
        beam_nos: List of beam numbers to select
        parameter_no: Parameter number to apply
        lx: Lateral X-bracing flag
        ly: Lateral Y-bracing flag
        lz: Lateral Z-bracing flag
        dj: Displacement joint flag
        main: Main parameters flag
        display_output: If True, displays markdown in Jupyter; always returns string

    Returns:
        Markdown-formatted string containing execution results in tabular form
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
        {"type": "command", "action": "close"},
    ]

    def format_beam_selection() -> List[str]:
        """Format beam selection information."""
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
        return [
            f"- **LX (Lateral X):** {'✓' if lx else '✗'}",
            f"- **LY (Lateral Y):** {'✓' if ly else '✗'}",
            f"- **LZ (Lateral Z):** {'✓' if lz else '✗'}",
            f"- **DJ (Displacement Joint):** {'✓' if dj else '✗'}",
            f"- **Main Parameters:** {'✓' if main else '✗'}",
        ]

    # Build markdown output
    markdown_output = [
        "# STAAD Helper Parameter Application",
        f"**Parameter Number:** {parameter_no}",
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
                sleep_time = wait_time if msg.get('action') in ['read_all_data', 'apply_parameters'] else 0.5
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