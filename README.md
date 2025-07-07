# Demo Project

This repository contains a Python script to transform SKU JSON data.  

### Files

- `transform.py`  
    Python script that:
    - Reads `mock.json` from the `S3/` folder
    - Extracts English values for:
        - Style Name
        - Vendor Name
        - Family Name
    - Outputs a simplified JSON file in `transformed_files/`

- `S3/mock.json`  
    Original large JSON file with SKU data.

- `transformed_files/transformed_sku.json`  
    Resulting JSON file with cleaned, simplified data.

### How to Run

```bash
python transform.py
