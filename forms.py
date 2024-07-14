import json
import os
import pandas as pd


filenames = ["product.json", "country.json"]
output_file = "forms.csv"

def read_json(json_file):
    """Reads a JSON file and returns a Python dictionary."""
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
    """Reads the dict object and returns a dataframe"""
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
    """Spool dataframe to a CSV file."""

    file_exists = os.path.isfile(output_file)
    file_is_empty = os.path.getsize(output_file) == 0 if file_exists else True
    
    try:
        details_df.to_csv(csv_file, mode = mode, index=False, encoding='utf-8', header=not file_exists or file_is_empty)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"File does not exist {e}")
    except Exception as e:
        raise Exception(f"An error occurred when saving data into CSV: {e}")


for filename in filenames:
    dataframe_to_csv(normalize_data(read_json(filename)), mode="a")