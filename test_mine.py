import json
import pprint

# Step 1: Load the original JSON data
with open('products.json', 'r') as f:
    data = json.load(f)

# Step 2: Extract the list of products
products = data.get("data", {}).get("products", [])

# Step 3: Transform each product into desired format
def extract_product_info(products):
    extracted = []
    for product in products:
        extracted.append({
            "id": product.get("id") or product.get("_id"),
            "Name": product.get("name"),
            "Description": product.get("description"),
            "Category": product.get("category", {}).get("name"),
            "URL": product.get("url"),
            "Profile Score(Created By)": product.get("createdBy", {}).get("profileScore"),
            "consensusScore": product.get("consensusScore"),
            "trustScore": product.get("trustScore"),
            "Marketing & Social Presence": product.get("twitterProfile"),
            "Current Review Cycle": product.get("currentReviewCycle"),
        })
    return extracted

# Step 4: Extract data
result = extract_product_info(products)

# Step 5: Save to a new JSON file
with open("extracted_products.json", "w") as f_out:
    json.dump(result, f_out, indent=2)

# Optional: Print preview
print("Saved to extracted_products.json")
pprint.pprint(result[:3])  # Preview first 3 items
