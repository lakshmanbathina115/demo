import json

print("Loading JSON...")

with open("/Users/lakshmanbathina/Desktop/demo/S3/mock.json", "r", encoding="utf-8") as f:
    data = json.load(f)

skus = data["Root"]["SKU"]

print(f"Total SKUs found: {len(skus)}")

output = []

def get_en_value(field):
    """Extract first English value from a multilingual field."""
    if isinstance(field, list):
        for lang_entry in field:
            if lang_entry.get("lang") == "en":
                content = lang_entry.get("content")
                if isinstance(content, list):
                    return content[0] if content else None
                return content
    return None

def to_float_list(str_list):
    """Convert list of strings to list of floats."""
    if isinstance(str_list, list):
        return [float(x) for x in str_list]
    return None

for i, sku in enumerate(skus, start=1):
    sku_data = {
        "Style Name": get_en_value(sku.get("Style Name")),
        "Vendor Name": get_en_value(sku.get("Vendor Name")),
        "Family Name": get_en_value(sku.get("Family Name")),
        "Embedding Vector": None,
        "Feature Vector": None,
        "Anchor Embedding": None,
        "Pair Embedding": None
    }

    part_link = sku["SKU_Part_Link"][0]
    font_file = part_link["Font_File"][0]

    sku_data["Embedding Vector"] = to_float_list(font_file.get("Embeddings Vector"))
    sku_data["Feature Vector"] = to_float_list(font_file.get("Feature Vector"))
    sku_data["Anchor Embedding"] = to_float_list(font_file.get("Anchor Embeddings"))
    sku_data["Pair Embedding"] = to_float_list(font_file.get("Pair Embeddings"))

    output.append(sku_data)

    print(f"Processed SKU {i}/{len(skus)} → Style: {sku_data['Style Name']}")

print("Saving transformed JSON...")

with open("/Users/lakshmanbathina/Desktop/demo/transformed_files/transformed_sku.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)

print("Done! Output saved to transformed_sku.json")
