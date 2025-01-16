"""Helper functions."""

def number_to_letter(number):
    """
    Converts a number (1-26) to its corresponding letter in the English alphabet.
    
    Args:
        number (int): The input number (1-26).
        
    Returns:
        str: The corresponding letter if the input is valid.
        
    Raises:
        ValueError: If the number is outside the range 1-26.
    """
    if not (1 <= number <= 26):
        raise ValueError("Input must be an integer between 1 and 26.")
    return str(chr(64 + number))

def round_float(n, precision):
    """
        Rounds a float to specified precision. If precision=0, convert to int.
        
        Args:
            n (float): Number to be rounded
            precision (int): Number of decimal places.
        
        Returns:
            r (float|int): Returns the rounded number.
    """
    if precision < 0:
        raise ValueError("Precision must be greater than or equal to zero.")
        
    return int(round(n, precision)) if precision == 0 else round(n, precision)

def full_path(gbt_filename, base_path=None):
    return gbt_filename if base_path is None else f"{base_path}/{gbt_filename}"