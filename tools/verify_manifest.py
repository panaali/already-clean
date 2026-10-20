"""Verify byte-preserved imported artifacts against their recorded SHA-256 and sizes."""
import hashlib
import json
from pathlib import Path
root = Path(__file__).resolve().parents[1]
manifest = json.loads((root / "provenance/manifest.json").read_text())
for entry in manifest["files"]:
    data = (root / entry["destination_path"]).read_bytes()
    assert len(data) == entry["bytes"], entry["destination_path"]
    assert hashlib.sha256(data).hexdigest() == entry["sha256"], entry["destination_path"]
print(f"Verified {len(manifest['files'])} preserved artifacts.")
