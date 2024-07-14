import glob
import json
import os
import pandas as pd


output_file = "forms.csv"
json_files = glob.glob('files/*.json')


def read_json(json_file):
    """
    Reads a JSON file and returns its contents as a dictionary.
    
    Parameters:
    json_file (str): The path to the JSON file to be read.

    Returns:
    dict: The contents of the JSON file as a dictionary.
    """
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            contents = json.load(file)
        return contents
    except EOFError as e:
        raise EOFError(f"File invalid: {e}")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File Not Found: {e}")
    except Exception as e:
        raise Exception(f"An error occurred: {e}")

def normalize_data(contents):
    """
    Reads a JSON (Python dict) and returns its contents as a pandas dataframe.
    
    Parameters:
    contents (dict): Contents extract from the JSON files.
    
    Returns:
    pandas dataframe: The JSON config normalized as a dataframe.
    """
        
    if "columns" not in contents:
        raise ValueError("The key 'columns' is missing from the JSON content.")
    try:
        details_df = pd.json_normalize(contents, record_path="columns", meta=["id"])    
        details_df["type_form"] = "form"
        return details_df
    except KeyError as e:
        raise KeyError(f"Missing key in JSON data: {e}")
    except Exception as e:
        raise Exception(f"An error occurred during normalization: {e}")

def dataframe_to_csv(details_df, csv_file=output_file, mode="w"):
    """
    Reads a dataframe and writes it into a CSV file.
    
    Parameters:
    details_df (pandas dataframe): Normalized dataframe from the JSON file read.
    csv_file (str): Output file to be written. Defaults to value in the "output_file".
    mode (str): Mode for writing the file. Defaults to "w" (write).

    Returns:
    None
   
    """

    file_exists = os.path.isfile(output_file)
    file_is_empty = os.path.getsize(output_file) == 0 if file_exists else True
    
    try:
        details_df.to_csv(csv_file, mode = mode, index=False, encoding='utf-8', header=not file_exists or file_is_empty)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File does not exist {e}")
    except Exception as e:
        raise Exception(f"An error occurred when saving data into CSV: {e}")


if __name__ == "__main__":
    for filename in json_files:
        dataframe_to_csv(normalize_data(read_json(filename)), mode="a")