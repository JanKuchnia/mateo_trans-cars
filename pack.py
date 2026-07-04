import json
import base64
import gzip
import re
import os

def main():
    original_html_path = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/index.html"
    src_dir = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/src"
    
    # Read the modified src/index.html template
    template_path = os.path.join(src_dir, "index.html")
    if not os.path.exists(template_path):
        print("Error: src/index.html not found!")
        return

    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()

    # Find all asset files in src_dir
    # Filenames are expected to be asset_<uuid>.<ext>
    asset_files = [f for f in os.listdir(src_dir) if f.startswith("asset_")]
    
    # We will reconstruct the manifest
    # First, let's load the original manifest to see compression settings or just determine based on file extension
    # JavaScript gets compressed, fonts do not.
    manifest = {}
    ext_resources = []
    
    for filename in asset_files:
        # Extract UUID
        # asset_669a5451-cdbb-4d83-9d6c-5115bc08d11c.js -> 669a5451-cdbb-4d83-9d6c-5115bc08d11c
        match = re.match(r'asset_([0-9a-f\-]+)\.(\w+)', filename)
        if not match:
            continue
        uuid = match.group(1)
        ext = match.group(2)
        
        filepath = os.path.join(src_dir, filename)
        with open(filepath, "rb") as f_asset:
            data = f_asset.read()
            
        # Determine mime type and compression
        compressed = False
        if ext == "js":
            mime = "text/javascript"
            compressed = True
        elif ext == "woff2":
            mime = "font/woff2"
            compressed = False
        else:
            mime = "application/octet-stream"
            compressed = False
            
        if compressed:
            compressed_data = gzip.compress(data)
            encoded_data = base64.b64encode(compressed_data).decode("utf-8")
        else:
            encoded_data = base64.b64encode(data).decode("utf-8")
            
        manifest[uuid] = {
            "mime": mime,
            "compressed": compressed,
            "data": encoded_data
        }
        
        # We also need to map the filename back to the UUID in the template
        template = template.replace(filename, uuid)
        
        # Add to ext_resources if needed
        # In the original file, ext_resources had entries like {"uuid": "...", "id": "..."}
        # but wait, since they were named asset_<uuid>.<ext> they weren't in ext_resources originally, or they had the same ID.
        # Let's check the original index.html to see what was in ext_resources.
        
    # Read the original index.html to find ext_resources and check if we can reuse it
    with open(original_html_path, "r", encoding="utf-8") as f_orig:
        orig_content = f_orig.read()
        
    ext_resources_match = re.search(r'<script type="__bundler/ext_resources">(.*?)</script>', orig_content, re.DOTALL)
    if ext_resources_match:
        ext_resources = json.loads(ext_resources_match.group(1).strip())
        # Filter ext_resources to only keep UUIDs that exist in our new manifest
        ext_resources = [e for e in ext_resources if e["uuid"] in manifest]

    # Convert template to JSON string as required by the loader
    # Escape </script> to <\/script> to prevent the HTML parser from ending the script tag early
    template_json = json.dumps(template).replace("</script>", "<\\/script>")
    manifest_json = json.dumps(manifest)
    ext_resources_json = json.dumps(ext_resources)

    # Reconstruct the original index.html by replacing script tags
    new_content = orig_content
    
    # Replace manifest
    new_content = re.sub(
        r'<script type="__bundler/manifest">.*?</script>',
        lambda m: f'<script type="__bundler/manifest">\n{manifest_json}\n</script>',
        new_content,
        flags=re.DOTALL
    )
    
    # Replace ext_resources
    new_content = re.sub(
        r'<script type="__bundler/ext_resources">.*?</script>',
        lambda m: f'<script type="__bundler/ext_resources">\n{ext_resources_json}\n</script>',
        new_content,
        flags=re.DOTALL
    )
    
    # Replace template
    new_content = re.sub(
        r'<script type="__bundler/template">.*?</script>',
        lambda m: f'<script type="__bundler/template">\n{template_json}\n</script>',
        new_content,
        flags=re.DOTALL
    )

    with open(original_html_path, "w", encoding="utf-8") as f_orig:
        f_orig.write(new_content)
        
    print("Pack completed successfully! index.html updated.")

if __name__ == "__main__":
    main()
