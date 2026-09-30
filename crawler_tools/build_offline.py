import os
import re
import shutil
from pathlib import Path

archive = Path(r"D:\ScaryJobs\mturk_archive")
offline_dir = archive / "offline_browsable"
offline_dir.mkdir(exist_ok=True)

# Copy all assets
assets_src = archive / "assets"
assets_dst = offline_dir / "assets"
if assets_dst.exists():
    shutil.rmtree(assets_dst)
shutil.copytree(assets_src, assets_dst)

# Also copy top-level pages
pages_dir = archive / "pages"
for html_file in pages_dir.rglob("*.html"):
    rel = html_file.relative_to(pages_dir)
    target = offline_dir / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    
    with open(html_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()
    
    # Calculate depth to offline_dir root
    depth = len(rel.parts) - 1
    root_rel = "../" * depth if depth > 0 else "./"
    
    # Fix absolute links to local pages
    content = re.sub(r'href=[\"\']/product-details[\"\']', f'href="{root_rel}product-details.html"', content)
    content = re.sub(r'href=[\"\']/pricing[\"\']', f'href="{root_rel}pricing.html"', content)
    content = re.sub(r'href=[\"\']/help[\"\']', f'href="{root_rel}help.html"', content)
    content = re.sub(r'href=[\"\']/resources[\"\']', f'href="{root_rel}resources.html"', content)
    content = re.sub(r'href=[\"\']/customers[\"\']', f'href="{root_rel}customers.html"', content)
    content = re.sub(r'href=[\"\']/worker[\"\']', f'href="{root_rel}worker.html"', content)
    content = re.sub(r'href=[\"\']/get-started[\"\']', f'href="{root_rel}get-started.html"', content)
    content = re.sub(r'href=[\"\']/participation-agreement[\"\']', f'href="{root_rel}participation-agreement.html"', content)
    content = re.sub(r'href=[\"\']/acceptable-use-policy[\"\']', f'href="{root_rel}acceptable-use-policy.html"', content)
    content = re.sub(r'href=[\"\']/privacy-notice[\"\']', f'href="{root_rel}privacy-notice.html"', content)
    content = re.sub(r'href=[\"\']/legal-licenses[\"\']', f'href="{root_rel}legal-licenses.html"', content)
    content = re.sub(r'href=[\"\']/mturk/findquals[\"\']', f'href="{root_rel}mturk/findquals.html"', content)
    content = re.sub(r'href=[\"\']/[\"\']', f'href="{root_rel}index.html"', content)
    
    # Point /assets/ to local assets/assets/
    content = re.sub(r'([\"\'\(])/assets/', r'\1' + root_rel + 'assets/assets/', content)
    
    with open(target, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Offline browsable site generated successfully in: {offline_dir}")
