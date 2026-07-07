import urllib.request
import urllib.parse
import re

def inspect_yahoo(query):
    url = f"https://search.yahoo.com/search?p={urllib.parse.quote(query)}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            # Look for "pexels" case-insensitive
            matches = re.findall(r'([^\s"\'<>]*pexels[^\s"\'<>]*)', html, re.IGNORECASE)
            print(f"Yahoo Search found {len(matches)} raw matches for 'pexels':")
            for m in list(set(matches))[:15]:
                print("-", m)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    inspect_yahoo("pexels tow truck")
