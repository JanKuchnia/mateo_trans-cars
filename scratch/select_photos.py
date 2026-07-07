import json

with open("/home/jankuchnia/Desktop/Mateo_Tran&Cars/scratch/pexels_results.json", "r") as f:
    data = json.load(f)

for category, photos in data.items():
    print(f"\n=================== {category.upper()} ===================")
    if not photos:
        print("No photos found.")
        continue
    for i, p in enumerate(photos[:3]):
        print(f"{i+1}. ID: {p['id']} | Photographer: {p['photographer']}")
        print(f"   Alt: {p['alt']}")
        print(f"   URL (1200/Hero): {p['url_1200']}")
        print(f"   URL (800/Grid):  {p['url_800']}")
