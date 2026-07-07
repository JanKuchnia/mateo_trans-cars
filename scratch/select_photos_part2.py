import json

with open("/home/jankuchnia/Desktop/Mateo_Tran&Cars/scratch/pexels_results.json", "r") as f:
    data = json.load(f)

categories = [
    "pomoc_drogowa_hero", "skutery_hero", "yamaha_jetski", 
    "seadoo_jetski", "kawasaki_jetski", "komis_hero", 
    "volkswagen_passat", "ford_transit", "skoda_octavia", "renault_master", "bmw_f30"
]

for category in categories:
    print(f"\n=================== {category.upper()} ===================")
    photos = data.get(category, [])
    if not photos:
        print("No photos found.")
        continue
    for i, p in enumerate(photos[:3]):
        print(f"{i+1}. ID: {p['id']} | Photographer: {p['photographer']}")
        print(f"   Alt: {p['alt']}")
        print(f"   URL (1200): {p['url_1200']}")
        print(f"   URL (800):  {p['url_800']}")
