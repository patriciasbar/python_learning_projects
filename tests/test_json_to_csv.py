import unittest
import os
import pandas as pd
from json_to_csv.forms import read_json, normalize_data, dataframe_to_csv

class TestForms(unittest.TestCase):
    def setUp(self):
        """Set up test sampling data."""
        self.json_files = "json_to_csv/files/product.json"
        self.contents = {
    "id": "countries",
    "columns": [
      {
        "display_name": "Country Num",
        "field_name": "ctry_num",
        "type": "number",
        "group": True,
        "sort": False
      },
      {
        "display_name": "Country",
        "field_name": "ctry",
        "type": "string",
        "group": True,
        "sort": False
      }      
    ],
    "type": "Form"
  }

    def test_read_json(self):
        """Test reading a valid JSON file."""
        result = read_json(self.json_files)
        self.assertIsInstance(result, dict)
        self.assertIn("columns", result)

    def test_normalize_json(self):
        """Test normalizing a valid DF"""
        details_df = pd.json_normalize(self.contents)    
        details_df["type_form"] = "form"
        self.assertIsInstance(details_df, pd.DataFrame)
        self.assertIn("type_form", details_df.columns)

    def test_dataframe_to_csv(self):
        """Test writing dataframe to CSV"""
        details_df = pd.json_normalize(self.contents)    
        output_file = os.path.join(os.path.dirname(__file__), "..", "test_output.csv") #got help from GPT in this one
        dataframe_to_csv(details_df, output_file)
        self.assertTrue(os.path.exists(output_file)) #got help from GPT in this one 
        os.remove(output_file)
            
    


if __name__ == "__main__":
    unittest.main()