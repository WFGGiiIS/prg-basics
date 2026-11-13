###
# Functions to read any data type from the keyboard
#
def input_string(message):
    new_message = input(message)
    return new_message

def input_integer(message):
    new_message = int(input(message))
    return new_message

def input_real(message):
    new_message = float(input(message))
    return new_message

def input_boolean(message):
    new_message = bool(input(message))
    return new_message
