version = "0.1.2"

# [0.1.2] - 2021-10-20
# --------------------
# - Added `is_writable` function to check if the user home directory is writable.
# - Added an `exception_handler` function to handle exceptions. Using traceback to print the error message.
# - Updated the `log_error` function by removing the errorType argument and checking if `is_writable` is True.