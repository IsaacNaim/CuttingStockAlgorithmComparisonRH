from Functions.excelinputextractor import generate_dictionaries
from Functions.EmadGoogleOR import StockCutter1D, drawGraph
from Functions.dictmodifier import add_blade_cut_lengths, multiply_keys_by_1000
import typer
# Define the file path and sheet name
file_path = 'inputfiles/comparison_results.xlsx'
sheet_name = 'Details'

# Generate the dictionaries
twoxfourinputs, twoxsixinputs = generate_dictionaries(file_path, sheet_name)
#add specified BCL, can specify length
twoxfourinputs, twoxsixinputs = (add_blade_cut_lengths(d,0.125) for d in (twoxfourinputs,twoxsixinputs))
# multiply out by 1000 (Google OR requires Integer Programming)
twoxfourinputs_integers, twoxsixinputs_integers = (multiply_keys_by_1000(d) for d in (twoxfourinputs, twoxsixinputs))



