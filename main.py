from Functions.excelinputextractor import generate_dictionaries

# Define the file path and sheet name
file_path = 'inputfiles/comparison_results.xlsx'
sheet_name = 'Details'

# Generate the dictionaries
twoxfourinputs, twoxsixinputs = generate_dictionaries(file_path, sheet_name)

def add_blade_cut_lengths(dict1, dict2, blade_cut_length=0.125):
    """
    Increment all the keys in the given dictionaries by the blade cut length value.
    """
    new_dict1 = {float(key) + blade_cut_length: value for key, value in dict1.items()}
    new_dict2 = {float(key) + blade_cut_length: value for key, value in dict2.items()}
    return new_dict1, new_dict2

twoxfourinputs, twoxsixinputs = add_blade_cut_lengths(twoxfourinputs, twoxsixinputs)

# Display the updated dictionaries
print("Updated 2x4rawinput:", twoxfourinputs)
print("Updated 2x6rawinput:", twoxsixinputs)