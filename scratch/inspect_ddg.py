import urllib.request
import urllib.parse
import re

def inspect_ddg(query):
    url = f"https://html.duckduckgo.com/html/?q={urllib.parse.quote(query)}"
    req = urllib.request.Request(
        url, 
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.0.0 Safari/537.36'}
    )
    try:
        with urllib.request.urlopen(req) as response:
            html = response.read().decode('utf-8')
            print("HTML length:", len(html))
            print("HTML start:", html[:500])
            
            hrefs = re.findall(r'href="([^"]+)"', html)
            print("Total hrefs found:", len(hrefs))
            for h in hrefs[:20]:
                print("HREF:", h)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    inspect_ddg("pexels tow truck")
