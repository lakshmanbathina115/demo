# Demo Project

This repository contains Python scripts to transform complex JSON data into simpler JSON and CSV formats for downstream processing and analytics.

---

## Contents

### Scripts

- `transform.py`
  - Processes font SKU JSON data
  - Extracts:
    - Style Name (English)
    - Vendor Name (English)
    - Family Name (English)
    - Embedding Vector
    - Feature Vector
    - Anchor Embedding
    - Pair Embedding
  - Outputs:
    - `transformed_files/transformed_sku.json`
    - `transformed_files/transformed_sku.csv`

- `transform2.py`
  - Processes Poster Image metadata from JSON
  - Extracts:
    - Family ID
    - PAS Legacy Id
    - Id_Font_Family_to_Digital_Assets_Production
    - DAMStatus_Font_Family_to_Digital_Assets_Production
    - Public URL_DAMMaster_to_DAMLink
    - IsActive_DAMMaster_to_DAMLink
    - IsPublic_DAMMaster_to_DAMLink
    - FilePath_DAMMaster_to_DAMLink
    - Image Priority_Font_Family_to_Digital_Assets_Production
  - Outputs:
    - `transformed_files/MFonts-Family-3666552.csv`

---

## How to Run

### 1. Run SKU Transform Script

```bash
python transform.py
