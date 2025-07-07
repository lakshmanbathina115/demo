import json

# Load your JSON file
with open("/Users/lakshmanbathina/Desktop/demo/S3/mock.json", "r", encoding="utf-8") as f:
    data = json.load(f)

skus = data["Root"]["SKU"]

output = []

for sku in skus:
    # Helper to extract EN value
    def get_en_value(field):
        if field and isinstance(field, list):
            for lang_entry in field:
                if lang_entry.get("lang") == "en":
                    content = lang_entry.get("content")
                    if isinstance(content, list):
                        return content[0] if content else None
                    return content
        return None
    
    sku_data = {
        "Style Name": get_en_value(sku.get("Style Name")),
        "Vendor Name": get_en_value(sku.get("Vendor Name")),
        "Family Name": get_en_value(sku.get("Family Name")),
    }
    output.append(sku_data)

# Save to new JSON
with open("/Users/lakshmanbathina/Desktop/demo/transformed_files/transformed_sku.json", "w", encoding="utf-8") as f:
    json.dump(output, f, indent=2, ensure_ascii=False)