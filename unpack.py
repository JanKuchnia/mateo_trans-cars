import json
import base64
import gzip
import re
import os
import mimetypes

def main():
    html_path = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/index.html"
    out_dir = "/home/jankuchnia/Desktop/Mateo_Tran&Cars/src"
    os.makedirs(out_dir, exist_ok=True)

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Regex to find script contents
    manifest_match = re.search(r'<script type="__bundler/manifest">(.*?)</script>', content, re.DOTALL)
    ext_resources_match = re.search(r'<script type="__bundler/ext_resources">(.*?)</script>', content, re.DOTALL)
    template_match = re.search(r'<script type="__bundler/template">(.*?)</script>', content, re.DOTALL)

    if not manifest_match or not template_match:
        print("Error: manifest or template not found!")
        return

    manifest = json.loads(manifest_match.group(1).strip())
    template = json.loads(template_match.group(1).strip())
    ext_resources = json.loads(ext_resources_match.group(1).strip()) if ext_resources_match else []

    uuid_to_filename = {}
    for entry in ext_resources:
        # entry matches format {"uuid": "...", "id": "..."}
        uuid_to_filename[entry["uuid"]] = entry["id"]

    # If any UUID is not in ext_resources, assign a default name based on mime type
    for uuid, entry in manifest.items():
        if uuid not in uuid_to_filename:
            mime = entry.get("mime", "application/octet-stream")
            ext = mimetypes.guess_extension(mime) or ".bin"
            uuid_to_filename[uuid] = f"asset_{uuid}{ext}"

    # Extract all assets
    for uuid, entry in manifest.items():
        filename = uuid_to_filename[uuid]
        filepath = os.path.join(out_dir, filename)
        
        # Ensure parent directories exist
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        # Decode base64
        data = base64.b64decode(entry["data"])
        
        # Decompress if compressed
        if entry.get("compressed", False):
            try:
                data = gzip.decompress(data)
            except Exception as e:
                print(f"Error decompressing {filename} ({uuid}): {e}")
                
        with open(filepath, "wb") as f_out:
            f_out.write(data)
        print(f"Extracted {filename} ({len(data)} bytes)")

    # Modify template to point to the local files instead of UUIDs
    for uuid, filename in uuid_to_filename.items():
        template = template.replace(uuid, filename)

    # Save template as index.html inside out_dir
    with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8") as f_out:
        f_out.write(template)
    print("Extracted template to src/index.html")

if __name__ == "__main__":
    main()
