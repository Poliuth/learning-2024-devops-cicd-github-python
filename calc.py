'''
The 'calc' library contains the 'add2' function that takes 2 values and adds
them together. If either value is a string (or both of them are) 'add2' ensures
they are both strings, thereby resulting in a concatenated result.
NOTE: If a value submitted to the 'add2' function is a float, it must be done so
in quotes (i.e. as a string).
'''

def conv(value):
    '''
    If 'value' is not an integer, convert it to a float and failing that, a string.

    Parameters:
    value (int, float, str): The value to be converted.

    Returns:
    int, float, str: The converted value.
    '''
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return str(value)

def add2(arg1, arg2):
    '''
    Ajoute un nombre quelconque d'arguments ensemble. Si un argument est une chaîne, tous sont traités comme des chaînes.
    '''
    converted_args = [conv(arg) for arg in args]
    if any(isinstance(arg, str) for arg in converted_args):
        return ''.join(map(str, converted_args))
    return sum(converted_args)
