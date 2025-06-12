from base.pipe_connection.pipe_client import PipeClient
import time

def apply_parameters_staad_helper(parameter_no):
    pipe_name = "STAAD_HELPER_PIPE"  # Should match your C# server pipe name

    messages = [
        {"type": "command", "action": "read_all_data"},
        {"type": "command", "action": "open_steel_tab"},
        {"type": "ui", "feature":"lx","payload":True},
        {"type": "ui", "feature":"ly","payload":True},
        {"type": "ui", "feature":"lz","payload":True},
        {"type": "ui", "feature":"dj","payload":False},
        {"type": "ui", "feature":"main","payload":True},
        {"type": "ui", "feature":"parameter","payload":parameter_no},
        {"type": "command", "action": "apply_parameters"},
    ]
    
    try:
        with PipeClient(pipe_name, timeout=10000) as client:
            for i, msg in enumerate(messages, 1):
                print(f"\nSending message {i}/{len(messages)}")
                response = client.send_json(msg)
                print(f"Response: {response}")
                time.sleep(0.5)  # Small delay between messages
                
    except ConnectionError as e:
        print(f"Connection failed: {e}")

if __name__ == "__main__":
    try:
        apply_parameters_staad_helper(1)
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Unexpected error: {e}")