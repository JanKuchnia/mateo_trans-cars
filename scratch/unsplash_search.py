import urllib.request
import urllib.parse
import re
import json
import time

def search_unsplash(query):
    url = f"https://unsplash.com/s/photos/{urllib.parse.quote(query)}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find URLs matching https://images.unsplash.com/photo-xxxxxxxxxxxxx?
            # We want the photo ID which comes after photo- and before ?
            matches = re.findall(r'https://images\.unsplash\.com/photo-([a-zA-Z0-9\-]+)', html)
            
            results = []
            seen = set()
            for pid in matches:
                if pid not in seen:
                    # Filter out small icon/profile photo ids (usually short)
                    if len(pid) > 8:
                        seen.add(pid)
                        results.append({
                            "id": pid,
                            "url": f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=800&q=80",
                            "url_large": f"https://images.unsplash.com/photo-{pid}?auto=format&fit=crop&w=1200&q=80"
                        })
            return results[:8]
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    queries = {
        "tow_truck": "tow truck",
        "car_dealership": "car dealership showroom",
        "delivery_van": "delivery van",
        "passenger_van": "passenger van minibus",
        "car_trailer": "car trailer",
        "jet_ski": "jet ski"
    }
    output = {}
    for key, q in queries.items():
        print(f"Searching Unsplash for: {key} ({q})")
        res = search_unsplash(q)
        output[key] = res
        time.sleep(1.0)
    print(json.dumps(output, indent=2))
