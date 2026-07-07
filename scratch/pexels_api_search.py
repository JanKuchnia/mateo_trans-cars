import os
import urllib.request
import urllib.parse
import json

def load_api_key():
    env_path = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/.env"
    if os.path.exists(env_path):
        with open(env_path, "r") as f:
            for line in f:
                if line.strip().startswith("PEXELS_API_KEY="):
                    return line.strip().split("PEXELS_API_KEY=")[1].strip()
    return None

def search_pexels(query, api_key, per_page=10):
    url = f"https://api.pexels.com/v1/search?query={urllib.parse.quote(query)}&per_page={per_page}"
    req = urllib.request.Request(url)
    req.add_header("Authorization", api_key)
    # Add User-Agent to avoid Cloudflare blocking
    req.add_header("User-Agent", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    try:
        with urllib.request.urlopen(req) as response:
            data = json.loads(response.read().decode('utf-8'))
            results = []
            for photo in data.get("photos", []):
                results.append({
                    "id": photo.get("id"),
                    "alt": photo.get("alt"),
                    "photographer": photo.get("photographer"),
                    "url_800": photo.get("src", {}).get("large"),     # 940px wide, ideal for grid cards
                    "url_1200": photo.get("src", {}).get("large2x"),   # 1880px wide, ideal for heroes
                    "url_original": photo.get("src", {}).get("original"),
                })
            return results
    except Exception as e:
        print(f"Error searching for '{query}': {e}")
        return []

if __name__ == "__main__":
    api_key = load_api_key()
    if not api_key:
        print("Error: PEXELS_API_KEY not found in .env file.")
        exit(1)
        
    searches = {
        # Roadside assistance
        "pomoc_drogowa_hero": "tow truck flatbed",
        
        # Jet skis
        "skutery_hero": "jet ski ocean action",
        "yamaha_jetski": "yamaha jet ski",
        "seadoo_jetski": "seadoo jet ski",
        "kawasaki_jetski": "kawasaki jet ski",
        
        # Dealership (Komis)
        "komis_hero": "car dealership lot outdoor",
        "volkswagen_passat": "volkswagen sedan",
        "ford_transit": "ford transit cargo van",
        "skoda_octavia": "station wagon car",
        "renault_master": "box truck cargo van",
        "bmw_f30": "bmw sedan",
        
        # Rental (Wypozyczalnia)
        "rental_hero": "cargo van delivery",
        "bus_winda": "box truck white",
        "bus_krotki": "short cargo van",
        "laweta_3_5t": "car transporter flatbed truck",
        "bus_9osobowy": "passenger van minibus",
        "przyczepa_laweta": "car trailer car hauler"
    }
    
    all_results = {}
    for key, query in searches.items():
        print(f"Searching Pexels for '{key}' using query '{query}'...")
        all_results[key] = search_pexels(query, api_key)
        
    output_path = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/scratch/pexels_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
        
    print(f"\nSearch complete! Results written to: {output_path}")
