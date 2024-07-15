import unittest
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
    
    


if __name__ == "__main__":
    unittest.main()