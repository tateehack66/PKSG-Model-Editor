from pathlib import Path
import base64
root=Path('.')
# Build #8 overlay is generated from the validated local asset pack.
# Binary sprite assets are embedded as base64 so GitHub Actions can recreate them.
ASSET_DIR = root / 'build8-assets'
print('Build 8 overlay bootstrap')
exec((root.parent / 'build8_overlay_payload.py').read_text()) if (root.parent / 'build8_overlay_payload.py').exists() else None
