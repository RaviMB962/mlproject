import sys
import logging

def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info() # 1st two info(exc_type, exc_obj) not required for us, hence not nominated those 

    file_name = exc_tb.tb_frame.f_code.co_filename ##this from exception handling document


    error_message = "Error Occured in Python Script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno,str(error))

    return error_message
    

class CustomException(Exception):
    def __init__(self, error_message, error_detail:sys):
        super().__init__(error_message) #inheriting here
        self.error_message=error_message_detail(error_message, error_detail=error_detail) 

    def __str__(self):
        return self.error_message
    

