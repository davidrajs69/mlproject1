import sys
from src.logger import logging

def error_message_detail(error, error_detail: sys):
    _,_,exec_tb = error_detail.exc_info()
    return f"Error occurred in script: {exec_tb.tb_frame.f_code.co_filename} at line number: {exec_tb.tb_lineno} error message: {str(error)}"

class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self):
        logging.info(self.error_message)
        return self.error_message

 
try:
    a = 1 / 0
except Exception as e:
    raise CustomException(e, sys)