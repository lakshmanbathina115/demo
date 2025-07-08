import json
import pandas as pd
from urllib.parse import urlparse

# Path to your JSON file
json_path = "/Users/lakshmanbathina/Desktop/demo/S3/Shopify-Family-Delta-3666552 (5).json"

# Load JSON
with open(json_path, "r", encoding="utf-8") as f:
    data = json.load(f)

records = []

# Loop through Font_Family objects
for family in data["Root"]["Font_Family"]:
    family_id = family.get("Family ID")
    pas_legacy_id = family.get("PAS Legacy Id")

    poster_links = family.get("Poster_Image_Link", [])
    for poster in poster_links:
        # Get Id_Font_Family_to_Digital_Assets_Production
        id_font_family_to_assets = poster.get("Id")

        # Get DAMStatus
        dam_status = poster.get("DAMStatus")

        # Get Public URL
        public_url = None
        poster_images = poster.get("Poster_Image")
        if poster_images and isinstance(poster_images, list):
            public_url = poster_images[0].get("Public URL")

        # Derive IsActive and IsPublic
        is_active = 'Y' if public_url else 'N'
        is_public = 'Yes' if public_url else 'No'

        # Derive FilePath_DAMMaster_to_DAMLink
        file_path = None
        if public_url:
            parsed = urlparse(public_url)
            path_parts = parsed.path.strip("/").split("/")
            # Expecting .../DAMRoot/Original/10000/filename.png
            if "Original" in path_parts:
                idx = path_parts.index("Original")
                if len(path_parts) > idx + 1:
                    file_path = "/".join(path_parts[idx + 1 :])

        # Get Image Priority
        image_priority = poster.get("Image Priority")

        record = {
            "Family ID": family_id,
            "PAS Legacy Id": pas_legacy_id,
            "Id_Font_Family_to_Digital_Assets_Production": id_font_family_to_assets,
            "DAMStatus_Font_Family_to_Digital_Assets_Production": dam_status,
            "Public URL_DAMMaster_to_DAMLink": public_url,
            "IsActive_DAMMaster_to_DAMLink": is_active,
            "IsPublic_DAMMaster_to_DAMLink": is_public,
            "FilePath_DAMMaster_to_DAMLink": file_path,
            "Image Priority_Font_Family_to_Digital_Assets_Production": image_priority,
        }

        records.append(record)

# Convert to DataFrame
df = pd.DataFrame(records)

# Set column order explicitly
df = df[
    [
        "Family ID",
        "PAS Legacy Id",
        "Id_Font_Family_to_Digital_Assets_Production",
        "DAMStatus_Font_Family_to_Digital_Assets_Production",
        "Public URL_DAMMaster_to_DAMLink",
        "IsActive_DAMMaster_to_DAMLink",
        "IsPublic_DAMMaster_to_DAMLink",
        "FilePath_DAMMaster_to_DAMLink",
        "Image Priority_Font_Family_to_Digital_Assets_Production",
    ]
]

# Save CSV
output_csv = "/Users/lakshmanbathina/Desktop/demo/transformed_files/MFonts-Family-3666552.csv"
df.to_csv(output_csv, index=False)

print(f"✅ DONE: {len(df)} rows saved to:\n{output_csv}")