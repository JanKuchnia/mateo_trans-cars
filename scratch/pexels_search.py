import urllib.request
import urllib.parse
import re
import json
import time

def search_pexels_via_ddg(query):
    # Formulate a query for DuckDuckGo targeting Pexels photos
    # e.g., site:pexels.com/photo "tow truck"
    full_query = f"site:pexels.com/photo {query}"
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(full_query)}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            
            # Find URLs that match pexels.com/photo/something-12345/ or similar
            # DuckDuckGo wraps links in /l/?kh=...&uddg=https%3A%2F%2Fwww.pexels.com%2Fphoto%2F...
            # Let's decode the hrefs or search for raw pexels.com%2Fphoto%2F matches
            matches = re.findall(r'pexels\.com%2Fphoto%2F([^%]+)-(\d+)%2F', html, re.IGNORECASE)
            
            # Also try raw URLs if present in snippet text
            matches2 = re.findall(r'pexels\.com/photo/([^/"]+)-(\d+)/', html, re.IGNORECASE)
            
            all_matches = matches + matches2
            
            results = []
            seen = set()
            for slug, pid in all_matches:
                slug_decoded = urllib.parse.unquote(slug)
                if pid not in seen:
                    seen.add(pid)
                    results.append({
                        "id": pid,
                        "slug": slug_decoded,
                        "url": f"https://images.pexels.com/photos/{pid}/pexels-photo-{pid}.jpeg",
                        "page": f"https://www.pexels.com/photo/{slug_decoded}-{pid}/"
                    })
            return results[:8]
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    queries = {
        "tow truck": "tow truck OR towing OR flatbed",
        "car dealership": "car dealership OR car dealer lot showroom",
        "delivery van": "delivery van cargo van",
        "passenger van": "passenger van minibus 9 seater",
        "car trailer": "car trailer car hauler utility trailer",
        "jet ski": "jet ski personal watercraft water scooter"
    }
    output = {}
    for key, q in queries.items():
        print(f"Searching DDG for: {key} ({q})")
        res = search_pexels_via_ddg(q)
        output[key] = res
        time.sleep(2.0)  # Rate limiting safety
    print(json.dumps(output, indent=2))
