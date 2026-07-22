"""ICML fetcher - proceedings.mlr.press"""
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from tqdm import tqdm
from .base import ConferenceFetcher

VOLUME_MAP = {2024: "v235", 2023: "v202", 2022: "v162"}
BASE_URL = "https://proceedings.mlr.press"

class ICMLFetcher(ConferenceFetcher):
    venue = "ICML"

    def __init__(self, year=2024):
        super().__init__()
        self.year = year

    def fetch(self):
        vol = VOLUME_MAP.get(self.year, "v235")
        index_url = f"{BASE_URL}/{vol}/"
        r = self._get(index_url)
        soup = BeautifulSoup(r.text, "html.parser")
        # Collect every paper-page link (/{vol}/<id>.html), robust to the wrapper markup.
        # (The old `div.paper a` selector broke when mlr.press changed its HTML.)
        pat = re.compile(rf"/{re.escape(vol)}/[^/]+\.html$")
        seen, links = set(), []
        for a in soup.find_all("a", href=True):
            full = urljoin(index_url, a["href"])
            if pat.search(full) and full not in seen:
                seen.add(full)
                links.append(full)
        papers = []
        for link in tqdm(links, desc=f"ICML {self.year}"):
            try:
                r = self._get(link)
                s = BeautifulSoup(r.text, "html.parser")
                title = s.find("h1")
                abstract = s.select_one("div#abstract")
                pdf = s.find("a", string=lambda t: t and "Download PDF" in t)
                if title and abstract:
                    papers.append(self._make_paper(
                        title=title.text,
                        abstract=abstract.text,
                        url=link,
                        pdf_url=pdf["href"] if pdf else "",
                        paper_id=link.split("/")[-1].replace(".html", ""),
                    ))
            except Exception as e:
                print(f"Failed {link}: {e}")
        return papers
