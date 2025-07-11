'''import json
from deepdiff import DeepDiff

# Paths to your JSON files
file1_path = "/Users/lakshmanbathina/Desktop/demo/S3/search-data - 2025-07-10T115226.024.json"
file2_path = "/Users/lakshmanbathina/Desktop/demo/S3/search-data - 2025-07-10T115235.694.json"

# Load both JSONs
with open(file1_path, "r", encoding="utf-8") as f1:
    data1 = json.load(f1)

with open(file2_path, "r", encoding="utf-8") as f2:
    data2 = json.load(f2)

# Compare entire JSON structures
diff = DeepDiff(data1, data2, ignore_order=True)

if diff:
    print("✅ Differences found between JSON files:")
    print(json.dumps(diff, indent=2))
else:
    print("✅ No differences found. JSONs are identical.")'''
import json

file1_path = "/Users/lakshmanbathina/Desktop/demo/S3/search-data - 2025-07-10T115226.024.json"
file2_path = "/Users/lakshmanbathina/Desktop/demo/S3/search-data - 2025-07-10T115235.694.json"

diffs_found = False

with open(file1_path, "r", encoding="utf-8") as f:
    data1 = json.load(f)

with open(file2_path, "r", encoding="utf-8") as f:
    data2 = json.load(f)

for i, (item1, item2) in enumerate(zip(data1, data2)):
    for key in set(item1.keys()).union(item2.keys()):
        if item1.get(key) != item2.get(key):
            diffs_found = True
            print(f"Family index {i}, key '{key}':")
            print("    File 1:", item1.get(key))
            print("    File 2:", item2.get(key))

if not diffs_found:
    print("✅ No differences found. JSON files are identical.")
