# Databricks notebook source
from datetime import datetime

current = datetime.now().strftime("%Y-%m-%d")

# COMMAND ----------

import requests
import json

all_characters = []
base_url = "https://dragonball-api.com/api/characters"
page = 1

while True:
    response = requests.get(f"{base_url}?page={page}")
    
    if response.status_code != 200:
        print(f"Failed to fetch page {page}: {response.status_code}")
        break

    data = response.json()
    
    # Append characters from this page
    if "items" in data:
        all_characters.extend(data["items"])
    else:
        print(f"No items found on page {page}")
        break
    
    # Check if we’ve reached the last page
    if page >= data.get("meta", {}).get("totalPages", 0):
        break

    page += 1

output_path = f"/Volumes/ctl_central_published/test_sc_dg_pg/ext_vol_pg/{current}_db_all_characters.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(all_characters, f, ensure_ascii=False, indent=4)

print(f"Saved {len(all_characters)} characters to {output_path}")
