#!/usr/bin/env python3
"""Fetch the machine-readable corpus sources listed in corpus/manifest.jsonl.

Usage: fetch_corpus.py [--tier 1|2]
- fetch=git entries are shallow-cloned into corpus/raw/<id>/ (skipped if present)
- fetch=api entries save their index JSON to corpus/raw/<id>.json
- fetch=manual entries are printed as a checklist (site/PDF sources, pull by hand)

Corpus data itself is gitignored; the manifest is the committed source of truth.
Every source in the manifest carries its license - check MODEL.md tiers before training.
"""
import json, subprocess, sys, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / "corpus" / "raw"

def main():
    tier = int(sys.argv[sys.argv.index("--tier") + 1]) if "--tier" in sys.argv else None
    RAW.mkdir(parents=True, exist_ok=True)
    for line in (ROOT / "corpus" / "manifest.jsonl").read_text().splitlines():
        src = json.loads(line)
        if tier and src["tier"] != tier:
            continue
        dest = RAW / src["id"]
        if src["fetch"] == "git":
            if dest.exists():
                print(f"skip {src['id']} (present)")
            else:
                print(f"clone {src['id']} <- {src['url']}")
                subprocess.run(["git", "clone", "--depth", "1", src["url"], str(dest)], check=False)
        elif src["fetch"] == "api":
            out = RAW / f"{src['id']}.json"
            if out.exists():
                print(f"skip {src['id']} (present)")
            else:
                print(f"api   {src['id']} <- {src['url']}")
                req = urllib.request.Request(src["url"], headers={"Accept": "application/json"})
                out.write_bytes(urllib.request.urlopen(req, timeout=60).read())
        else:
            print(f"manual {src['id']}: {src['url']} [{src['license']}]")

if __name__ == "__main__":
    main()
