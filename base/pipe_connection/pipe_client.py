import json
import time
import logging
from typing import Dict, Any, Optional, Union
import win32pipe
import win32file
import pywintypes

class PipeClient:
    """
    Python client for connecting to Windows Named Pipes and sending JSON data.
    Compatible with the C# PipeServer implementation.
    """
    
    def __init__(self, pipe_name: str, timeout: int = 5000):
        """
        Initialize the pipe client.
        
        Args:
            pipe_name (str): Name of the pipe (without \\\\.\\pipe\\ prefix)
            timeout (int): Connection timeout in milliseconds
        """
        self.pipe_name = pipe_name
        self.pipe_path = f"\\\\.\\pipe\\{pipe_name}"
        self.timeout = timeout
        self.handle = None
        self.is_connected = False
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def connect(self) -> bool:
        """
        Connect to the named pipe server.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.logger.info(f"Attempting to connect to pipe: {self.pipe_path}")
            
            # Wait for the pipe to become available
            win32pipe.WaitNamedPipe(self.pipe_path, self.timeout)
            
            # Open the pipe
            self.handle = win32file.CreateFile(
                self.pipe_path,
                win32file.GENERIC_READ | win32file.GENERIC_WRITE,
                0,  # No sharing
                None,  # Default security
                win32file.OPEN_EXISTING,
                0,  # Default attributes
                None  # No template
            )
            
            self.is_connected = True
            self.logger.info("Successfully connected to pipe server")
            return True
            
        except pywintypes.error as e:
            self.logger.error(f"Failed to connect to pipe: {e}")
            self.is_connected = False
            return False
        except Exception as e:
            self.logger.error(f"Unexpected error during connection: {e}")
            self.is_connected = False
            return False
    
    def disconnect(self):
        """Disconnect from the pipe server."""
        if self.handle:
            try:
                win32file.CloseHandle(self.handle)
                self.logger.info("Disconnected from pipe server")
            except Exception as e:
                self.logger.error(f"Error during disconnection: {e}")
            finally:
                self.handle = None
                self.is_connected = False
    
    def send_json(self, data: Union[Dict[str, Any], list, str, int, float, bool]) -> Optional[str]:
        """
        Send JSON data to the pipe server and receive response.
        
        Args:
            data: Data to be serialized as JSON and sent
            
        Returns:
            str: Response from server, or None if error occurred
        """
        if not self.is_connected or not self.handle:
            self.logger.error("Not connected to pipe server")
            return None
        
        try:
            # Serialize data to JSON
            json_data = json.dumps(data, ensure_ascii=False, indent=None)
            message_bytes = json_data.encode('utf-8')
            
            self.logger.info(f"Sending JSON data: {json_data}")
            
            # Send data to server
            win32file.WriteFile(self.handle, message_bytes)
            
            # Read response from server
            result, response_bytes = win32file.ReadFile(self.handle, 4096)
            response = response_bytes.decode('utf-8')
            
            self.logger.info(f"Received response: {response}")
            return response
            
        except pywintypes.error as e:
            self.logger.error(f"Pipe communication error: {e}")
            return None
        except json.JSONEncodeError as e:
            self.logger.error(f"JSON serialization error: {e}")
            return None
        except Exception as e:
            self.logger.error(f"Unexpected error during communication: {e}")
            return None
    
    def send_message(self, message: str) -> Optional[str]:
        """
        Send a plain text message to the pipe server.
        
        Args:
            message (str): Message to send
            
        Returns:
            str: Response from server, or None if error occurred
        """
        if not self.is_connected or not self.handle:
            self.logger.error("Not connected to pipe server")
            return None
        
        try:
            message_bytes = message.encode('utf-8')
            self.logger.info(f"Sending message: {message}")
            
            # Send message
            win32file.WriteFile(self.handle, message_bytes)
            
            # Read response
            result, response_bytes = win32file.ReadFile(self.handle, 4096)
            response = response_bytes.decode('utf-8')
            
            self.logger.info(f"Received response: {response}")
            return response
            
        except Exception as e:
            self.logger.error(f"Error sending message: {e}")
            return None
    
    def __enter__(self):
        """Context manager entry."""
        if self.connect():
            return self
        else:
            raise ConnectionError("Failed to connect to pipe server")
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()


class JsonPipeClient:
    """
    High-level client specifically designed for JSON communication.
    Includes additional features like retry logic and structured responses.
    """
    
    def __init__(self, pipe_name: str, max_retries: int = 3, retry_delay: float = 1.0):
        """
        Initialize the JSON pipe client.
        
        Args:
            pipe_name (str): Name of the pipe
            max_retries (int): Maximum number of connection retries
            retry_delay (float): Delay between retries in seconds
        """
        self.pipe_name = pipe_name
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        self.logger = logging.getLogger(__name__)
    
    def send_json_with_retry(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Send JSON data with automatic retry logic.
        
        Args:
            data (dict): Data to send as JSON
            
        Returns:
            dict: Result dictionary with success status and response/error
        """
        last_error = None
        
        for attempt in range(self.max_retries):
            try:
                with PipeClient(self.pipe_name) as client:
                    response = client.send_json(data)
                    if response:
                        return {
                            'success': True,
                            'response': response,
                            'attempt': attempt + 1
                        }
                    else:
                        last_error = "No response received"
                        
            except Exception as e:
                last_error = str(e)
                self.logger.warning(f"Attempt {attempt + 1} failed: {e}")
            
            if attempt < self.max_retries - 1:
                time.sleep(self.retry_delay)
        
        return {
            'success': False,
            'error': last_error,
            'attempts': self.max_retries
        }
