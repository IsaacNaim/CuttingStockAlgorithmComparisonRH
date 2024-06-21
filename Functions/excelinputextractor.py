import pandas as pd

def generate_dictionaries(file_path, sheet_name):
    """
    Reads an Excel file and generates two dictionaries from specified columns.
    
    Parameters:
    file_path (str): Path to the Excel file.
    sheet_name (str): Name of the sheet to read.
    
    Returns:
    dict1 (dict): Dictionary with keys from the first column and values from the second column.
    dict2 (dict): Dictionary with keys from the third column and values from the fourth column.
    """
    try:
        # Read the specified sheet into a DataFrame
        df = pd.read_excel(file_path, sheet_name=sheet_name,header=0)
        
        # Create the first dictionary from columns 1 and 2
        dict1 = pd.Series(df.iloc[:, 1].values, index=df.iloc[:, 0]).dropna().to_dict()
        
        # Create the second dictionary from columns 4 and 5
        dict2 = pd.Series(df.iloc[:, 4].values, index=df.iloc[:, 3]).dropna().to_dict()
                # Filter out entries where keys or values contain strings
        dict1 = {k: v for k, v in dict1.items() if not isinstance(k, str) and not isinstance(v, str)}
        dict2 = {k: v for k, v in dict2.items() if not isinstance(k, str) and not isinstance(v, str)}
        sorted_dict1 = {k: dict1[k] for k in sorted(dict1)}
        sorted_dict2 = {k: dict2[k] for k in sorted(dict2)}
        return sorted_dict1, sorted_dict2
    
    except Exception as e:
        print(f"An error occurred: {e}")
        return None, None
