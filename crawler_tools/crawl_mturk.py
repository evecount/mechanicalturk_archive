import os
import re
import sys
import time
import urllib.request
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

BASE_URL = "https://www.mturk.com"
ARCHIVE_DIR = Path(r"D:\ScaryJobs\mturk_archive")
PAGES_DIR = ARCHIVE_DIR / "pages"
ASSETS_DIR = ARCHIVE_DIR / "assets"
RAW_DIR = ARCHIVE_DIR / "raw"

ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
PAGES_DIR.mkdir(parents=True, exist_ok=True)
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
RAW_DIR.mkdir(parents=True, exist_ok=True)

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"

visited_urls = set()
urls_to_visit = set([
    "https://www.mturk.com/",
    "https://www.mturk.com/overview",
    "https://www.mturk.com/features",
    "https://www.mturk.com/pricing",
    "https://www.mturk.com/help",
    "https://www.mturk.com/developer-resources",
    "https://www.mturk.com/customers",
    "https://www.mturk.com/worker",
    "https://www.mturk.com/get-started",
    "https://www.mturk.com/robots.txt",
    "https://www.mturk.com/sitemap.xml",
])

downloaded_assets = set()

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            content_type = resp.headers.get("Content-Type", "")
            data = resp.read()
            return data, content_type
    except Exception as e:
        print(f"[-] Error fetching {url}: {e}")
        return None, None

class LinkExtractor(HTMLParser):
    def __init__(self, page_url):
        super().__init__()
        self.page_url = page_url
        self.links = set()
        self.assets = set()

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        
        # href
        if "href" in attr_dict:
            href = attr_dict["href"].strip()
            if href and not href.startswith("javascript:") and not href.startswith("mailto:") and not href.startswith("tel:"):
                full_url = urllib.parse.urljoin(self.page_url, href)
                # Check if asset
                parsed = urllib.parse.urlparse(full_url)
                ext = Path(parsed.path).suffix.lower()
                if ext in [".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg", ".ico", ".webp", ".woff", ".woff2", ".ttf", ".pdf"]:
                    self.assets.add(full_url)
                else:
                    self.links.add(full_url)

        # src
        if "src" in attr_dict:
            src = attr_dict["src"].strip()
            if src and not src.startswith("data:"):
                full_url = urllib.parse.urljoin(self.page_url, src)
                self.assets.add(full_url)

        # srcset
        if "srcset" in attr_dict:
            srcset = attr_dict["srcset"]
            for part in srcset.split(","):
                u = part.strip().split(" ")[0]
                if u and not u.startswith("data:"):
                    self.assets.add(urllib.parse.urljoin(self.page_url, u))

def url_to_filename(url, prefix_dir, default_ext=".html"):
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    if not path or path.endswith("/"):
        path += "index"
    
    # Clean path
    path = re.sub(r'[^a-zA-Z0-9_\-\./]', '_', path)
    if path.startswith("/"):
        path = path[1:]
    
    p = prefix_dir / path
    if not p.suffix:
        p = p.with_suffix(default_ext)
    return p

print("[*] Starting discovery...")

# First fetch robots.txt and sitemap.xml
for special in ["https://www.mturk.com/robots.txt", "https://www.mturk.com/sitemap.xml"]:
    data, ct = fetch(special)
    if data:
        fn = RAW_DIR / special.split("/")[-1]
        with open(fn, "wb") as f:
            f.write(data)
        print(f"[+] Saved {special} -> {fn}")
        if special.endswith(".xml"):
            # extract urls from sitemap
            sitemap_urls = re.findall(r'<loc>(https?://[^<]+)</loc>', data.decode('utf-8', errors='ignore'))
            for su in sitemap_urls:
                if "mturk.com" in su:
                    urls_to_visit.add(su)
            print(f"[+] Found {len(sitemap_urls)} URLs in sitemap")

# Now crawl
while urls_to_visit:
    url = urls_to_visit.pop()
    
    # Strip fragment and query for normalization if needed
    parsed = urllib.parse.urlparse(url)
    clean_url = urllib.parse.urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip('/'), '', '', ''))
    if not clean_url:
        clean_url = url
    
    if clean_url in visited_urls:
        continue
    visited_urls.add(clean_url)
    
    # Only follow mturk.com domain
    if parsed.netloc not in ["www.mturk.com", "mturk.com"]:
        print(f"[*] Skipping external domain: {url}")
        continue
        
    print(f"[*] Scraping page: {url}")
    data, ct = fetch(url)
    if not data:
        continue
        
    # Save page
    save_path = url_to_filename(url, PAGES_DIR, default_ext=".html")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    with open(save_path, "wb") as f:
        f.write(data)
    print(f"[+] Saved page to {save_path.name}")
    
    # If HTML, extract links & assets
    if "html" in ct or ct == "" or save_path.suffix == ".html":
        try:
            html_text = data.decode("utf-8", errors="ignore")
            parser = LinkExtractor(url)
            parser.feed(html_text)
            
            for l in parser.links:
                lp = urllib.parse.urlparse(l)
                if lp.netloc in ["www.mturk.com", "mturk.com"]:
                    clean_l = urllib.parse.urlunparse((lp.scheme, lp.netloc, lp.path.rstrip('/'), '', '', ''))
                    if clean_l not in visited_urls:
                        urls_to_visit.add(l)
            
            for a in parser.assets:
                if a not in downloaded_assets:
                    downloaded_assets.add(a)
        except Exception as e:
            print(f"[-] Error parsing HTML for {url}: {e}")

print(f"\n[*] Total pages visited: {len(visited_urls)}")
print(f"[*] Total assets found: {len(downloaded_assets)}")
print("[*] Downloading assets...")

for i, asset_url in enumerate(downloaded_assets):
    parsed = urllib.parse.urlparse(asset_url)
    # allow downloading assets from mturk.com or cdn (like amazonaws, cloudfront, etc. if referenced)
    save_path = url_to_filename(asset_url, ASSETS_DIR, default_ext=".bin")
    save_path.parent.mkdir(parents=True, exist_ok=True)
    
    if save_path.exists():
        continue
        
    print(f"[{i+1}/{len(downloaded_assets)}] Asset: {asset_url}")
    data, ct = fetch(asset_url)
    if data:
        with open(save_path, "wb") as f:
            f.write(data)
    time.sleep(0.05)

print("\n[+] CRAWL COMPLETE!")
