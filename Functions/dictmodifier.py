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
    print('listoflist')
    print(listoflists)
    return listoflists

def round_blade_cut(input_listoflists):
    parent_width = 192000
    threshold = parent_width + (0.125*1000) #multiplied by 1000 bc did that for keys
    for i, item in enumerate(input_listoflists):
        if item[1] >= threshold:
            input_listoflists[i][1] = int(input_listoflists[i][1] - (0.125*1000))
    return input_listoflists

