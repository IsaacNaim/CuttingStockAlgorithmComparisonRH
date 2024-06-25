import math

def add_blade_cut_lengths(dict1, blade_cut_length=0.125):
    """
    Increment all the keys in the given dictionaries by the blade cut length value.
    """
    new_dict = {float(key) + blade_cut_length: value for key, value in dict1.items()}
    return new_dict

def multiply_keys_by_1000(input_dict):
    """Multiply all keys in the dictionary by 1000 to convert them to whole numbers."""
    multiplied_dict = {int(key * 1000): value for key, value in input_dict.items()}
    return multiplied_dict

def convert_dict_to_Google_OR_format(input_dict):
    listoflists = []
    for key, value in input_dict.items():
        listoflists.append([value,key])
    return listoflists

def round_blade_cut(input_listoflists):
    for sublist in input_listoflists:
        sublist[1] = math.ceil(sublist[1] / 100)
    print(input_listoflists)
    return input_listoflists
