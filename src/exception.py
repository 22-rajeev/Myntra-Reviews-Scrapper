import sys
import os

def error_message_detail(error, error_detail: sys):
    try:
        exc_type, exc_obj, exc_tb = error_detail.exc_info()
        if exc_tb is not None:
            file_name = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            return "Error occurred in python script [{0}] line number [{1}] error message [{2}]".format(
                file_name, exc_tb.tb_lineno, str(error)
            )
        else:
            # No traceback → just return error text
            return f"Error message [{str(error)}]"
    except Exception:
        return str(error)


class CustomException(Exception):
    def __init__(self, error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_detail=error_detail
        )

    def __str__(self):
        return self.error_message