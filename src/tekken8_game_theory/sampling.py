import random

def sample_based_on_percentage(data: dict, n: int):
    """
    Samples `n` random keys from the dictionary `data` based on their percentage values.

    :param data: A dictionary where keys are strings and values are percentages (must sum up to 100).
    :param n: The number of samples to draw.
    :return: A list of `n` sampled keys.
    """
    if not isinstance(data, dict) or not all(isinstance(v, (int, float)) for v in data.values()):
        raise ValueError("Input must be a dictionary with numeric percentage values.")

    keys = list(data.keys())
    weights = list(data.values())
    return random.choices(keys, weights=weights, k=n)