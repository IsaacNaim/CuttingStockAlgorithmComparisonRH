from Functions.excelinputextractor import generate_dictionaries
from Functions.EmadGoogleOR import StockCutter1D, drawGraph
from Functions.dictmodifier import add_blade_cut_lengths, multiply_keys_by_1000, convert_dict_to_Google_OR_format,round_blade_cut
import typer
# Define the file path and sheet name
file_path = 'inputfiles/comparison_results.xlsx'
sheet_name = 'Details'

# Generate the dictionaries
twoxfourinputs, twoxsixinputs = generate_dictionaries(file_path, sheet_name)
#add specified BCL, can specify length
blade_cut_length = 0.1
twoxfourinputs, twoxsixinputs = (add_blade_cut_lengths(d,blade_cut_length) for d in (twoxfourinputs,twoxsixinputs))
# multiply out by 1000 (Google OR requires Integer Programming)
twoxfourinputs_integers, twoxsixinputs_integers = (multiply_keys_by_1000(d) for d in (twoxfourinputs, twoxsixinputs))
# required format for Google OR is list of [quantity, width]
twoxfourinputs_integers_listoflists = convert_dict_to_Google_OR_format(twoxfourinputs_integers)
# dividing all keys by 10 and rounding up, to speed runtime
twoxfourinputs_integers_listoflists = round_blade_cut(twoxfourinputs_integers_listoflists)

# Example parent rolls
parent_rolls = [[10, 1920]]  #10 is a placeholder

def main():
    # Call the StockCutter1D function with the provided child and parent rolls
    consumed_big_rolls = StockCutter1D(blade_cut_length,twoxfourinputs_integers_listoflists, parent_rolls, output_json=False, large_model=False)

    print(f"Consumed big rolls: {consumed_big_rolls}")
if __name__ == "__main__":
    main()