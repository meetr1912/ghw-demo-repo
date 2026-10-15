# Social preview image

GitHub shows this 1280×640 card whenever the repository link is unfurled (Slack,
X/Twitter, Discord, etc.). Upload it under
**Repository → Settings → General → Social preview**.

## Files

| File | What it is |
| --- | --- |
| `social-preview.png` | **The artifact to upload.** 1280×640, RGB, ~60 KB (limit is 1 MB). |
| `make_social_preview.py` | Pillow script that generates the PNG. |
| `social-preview.svg` | Dependency-free vector source (alternate render path). |

## Regenerate

```bash
# Canonical (uses Pillow; DejaVu fonts ship with the dev container image)
python3 make_social_preview.py        # -> social-preview.png (1280x640)

# SVG fallback if Pillow is unavailable
rsvg-convert -w 1280 -h 640 social-preview.svg -o social-preview.png
```

GitHub requirements: **PNG / JPG / GIF, ≤ 1 MB, recommended 1280×640 (2:1)**.
