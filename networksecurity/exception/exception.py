import sys
from networksecurity.logging import logger

class NetworkSecurityException(Exception):
    """Base class for all exceptions raised by the Network Security module."""
    def __init__(self, error_message,error_details:sys):
        def __init__(self, error_message, error_details:sys):
            
            self.error_message = error_message
            _,_,exc_tb = error_details.exc_info()

            self.file_name = exc_tb.tb_frame.f_code.co_filename
            self.line_number = exc_tb.tb_lineno


        def __str__(self):
                return f"Error occurred in script: {self.file_name} at line: {self.line_number} with message: {self.error_message}"

