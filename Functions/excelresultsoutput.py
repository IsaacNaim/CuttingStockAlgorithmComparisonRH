import pandas as pd

def write_results_to_excel(rolls, rolls1, waste_percentage, waste_percentage1):
    # Divide all values in rolls and rolls1 by 1000

    # Create a DataFrame to store the results
        # Find the maximum length of sublists in rolls and rolls1
    max_length = max(len(rolls), len(rolls1))
    
    # Create lists for each column
    rolls_column = []
    rolls1_column = []

    # Populate the columns with data
    for i in range(max_length):
        rolls_column.append(rolls[i] if i < len(rolls) else [])
        rolls1_column.append(rolls1[i] if i < len(rolls1) else [])

    # Create DataFrame with two columns
    df = pd.DataFrame({
        'Rolls': rolls_column,
        'Rolls1': rolls1_column
    })
    summary_data = {
        "Type": ["2x4", "2x6"],
        "Waste Percentage": [waste_percentage, waste_percentage1],
        "Total Rolls Used": [len(rolls), len(rolls1)],
        "Total Length Used": [sum(sum(roll) for roll in rolls), sum(sum(roll) for roll in rolls1)]
    }
    
    df_summary = pd.DataFrame(summary_data)

    
    # Write to Excel file
    output_file_path = 'outputfiles/cutting_stock_results.xlsx'
    with pd.ExcelWriter(output_file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Rolls', index=False)
        df_summary.to_excel(writer, sheet_name='Summary', index=False)
    print(f"Results have been written to {output_file_path}")
