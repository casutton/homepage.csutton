# /// script
# requires-python = ">=3.11"
# dependencies = ["bibtexparser>=2.0.0b7", "jinja2>=3.1", "pylatexenc>=2.10"]
# ///
"""Build the publications page fragments from papers.bib.

    uv run pubs/build.py            # writes _includes/pubs-by-year.html, pubs-by-topic.html, top-cited.html
                                    # (Jekyll then includes them in publications.html etc.; CI runs this on every push)
    uv run pubs/build.py --preview  # also writes pubs/preview/*.html (full pages, using the live site's
                               # header/CSS as a shell) and opens them in the browser

Replaces the old bibtool + bibout + Makefile pipeline. Same templates, same HTML.

Special BibTeX fields used (same as before):
  keywords   comma-separated topics for the by-topic page
  myurl      main link (falls back to url)
  arxivurl, codeurl, dataurl, website, openreviewurl -> extra links
  annote, webnote, arxivstring -> notes shown on the page
"""

import re
import sys
from collections import defaultdict
from pathlib import Path

import bibtexparser
from bibtexparser.middlewares import RemoveEnclosingMiddleware
from bibtexparser.middlewares.names import parse_single_name_into_parts, split_multiple_persons_names
from jinja2 import Environment, FileSystemLoader
from pylatexenc.latex2text import LatexNodes2Text

ROOT = Path(__file__).parent
BIB = ROOT / "papers.bib"
TOP_CITED = ROOT / "top-cited.txt"  # BibTeX keys for the home page's "Selected Publications"
OUT = ROOT.parent / "_includes"   # the Jekyll site's includes dir
PREVIEW = ROOT / "preview"

# Fields kept in the "bib" popup (everything else, e.g. abstract/keywords/myurl, is stripped).
STANDARD_FIELDS = [
    "address", "annote", "author", "booktitle", "chapter", "crossref", "edition", "editor",
    "howpublished", "institution", "journal", "month", "number", "organization", "pages",
    "publisher", "school", "series", "title", "type", "volume", "year",
]
NAME_FIELDS = {"author", "editor"}
MONTHS = {m: m[:3].lower() for m in ["January", "February", "March", "April", "May", "June", "July",
                                      "August", "September", "October", "November", "December"]}

_latex = LatexNodes2Text(math_mode="verbatim")


def delatex(s: str) -> str:
    s = re.sub(r"\s+", " ", s).strip()
    s = re.sub(r"(?<!\\)([%&])", r"\\\1", s)  # bare % and & are literal text in our bib, not LaTeX syntax
    return _latex.latex_to_text(s)


def parse_names(raw: str) -> list[tuple[str, str, str, str]]:
    """Return list of (first, von, last, jr), LaTeX-decoded."""
    out = []
    for n in split_multiple_persons_names(re.sub(r"\s+", " ", raw).strip()):
        p = parse_single_name_into_parts(n)
        out.append(tuple(delatex(" ".join(part)) for part in (p.first, p.von, p.last, p.jr)))
    return out


def display_name(n) -> str:  # "Charles Sutton"
    return " ".join(x for x in (n[0], n[1], n[2], n[3]) if x)


def sort_name(n) -> str:  # "Sutton, Charles"
    return ", ".join(x for x in (" ".join(x for x in (n[1], n[2]) if x), n[3], n[0]) if x)


def pretty_names(names) -> str:
    d = [display_name(n) for n in names]
    return d[0] if len(d) == 1 else ", ".join(d[:-1]) + " and " + d[-1]


def load_entries(path: Path) -> list[dict]:
    # No @string resolution, so month = jun stays "jun" (as the old build showed it).
    lib = bibtexparser.parse_string(path.read_text(encoding="utf-8"), parse_stack=[RemoveEnclosingMiddleware()])
    for block in lib.failed_blocks:
        print(f"warning: could not parse block near: {block.raw[:80]!r}", file=sys.stderr)
    entries = []
    for ent in lib.entries:
        e = {"type": ent.entry_type.lower(), "key": ent.key}
        bib_fields = []
        for f in ent.fields:
            name = f.key.lower()
            raw = str(f.value)
            if name in NAME_FIELDS:
                names = parse_names(raw)
                bibval = " and ".join(sort_name(n) for n in names)
                # authors display as "A, B and C"; editors were shown in "Last, First and ..." form
                e[name] = pretty_names(names) if name == "author" else bibval
                if name == "author":
                    e["authors"] = e[name]
            else:
                e[name] = delatex(raw)
                if name == "month":  # bibtexparser expands `jun` to "June"; keep the abbreviation
                    e[name] = MONTHS.get(e[name], e[name])
                elif not (name.endswith("url") or name == "website"):
                    e[name] = e[name].replace("'", "\u2019")  # typographic apostrophe, as before
                bibval = e[name]
            if name in STANDARD_FIELDS:
                bib_fields.append((name, bibval))
        e["bibtex"] = (
            f"@{e['type']}{{{e['key']},\n"
            + ",\n".join(f"  {k} = {{{v}}}" for k, v in bib_fields)
            + "\n}\n"
        )
        if not (e.get("myurl") or e.get("url") or e.get("arxivurl")):
            print(f"warning: no URL for {e['key']}", file=sys.stderr)
        venue = {"article": "journal", "inproceedings": "booktitle", "incollection": "booktitle",
                 "techreport": "institution", "phdthesis": "school"}.get(e["type"])
        if venue and not e.get(venue):
            print(f"warning: @{e['type']} {e['key']} has no {venue} (will show as '. .')", file=sys.stderr)
        entries.append(e)
    return entries


def year_int(e) -> int:
    try:
        return int(e.get("year", ""))
    except ValueError:
        return 9999


def build(entries: list[dict]) -> dict[str, dict]:
    # by year (newest first; file order within a year)
    by_year = defaultdict(list)
    for e in entries:
        by_year[e.get("year", "")].append(e)
    by_year = sorted(by_year.items(), key=lambda kv: kv[0], reverse=True)

    # by topic
    topics = sorted({k.strip() for e in entries for k in e.get("keywords", "").split(",") if k.strip()})
    by_topic = {t: [e for e in entries if t in e.get("keywords", "")] for t in topics}
    topic_order = sorted(topics, key=lambda t: (max(year_int(e) for e in by_topic[t]), len(by_topic[t])), reverse=True)
    by_topic = [(t, sorted(by_topic[t], key=year_int, reverse=True)) for t in topic_order]

    # most cited (home page), keys listed in top-cited.txt
    by_key = {e["key"]: e for e in entries}
    keys = [line.split("#")[0].strip() for line in TOP_CITED.read_text().splitlines()]
    top_cited = [by_key[k] for k in keys if k]

    return {
        "pubs-by-year.html": {"by_year": by_year},
        "pubs-by-topic.html": {"topics_alpha": topics, "by_topic": by_topic},
        "top-cited.html": {"top_cited": top_cited},
    }


LIVE = "https://homepages.inf.ed.ac.uk/csutton/"
PREVIEW_PAGES = {  # fragment -> (live page used as the shell, marker where the fragment starts)
    "pubs-by-year.html": ("publications.html", '<h3 class="year">'),
    "pubs-by-topic.html": ("publications-by-topic.html", "<!-- Header listing keywords -->"),
}


def preview():
    """Splice freshly built fragments into copies of the live pages, so we can see the real look locally."""
    import subprocess
    import urllib.request

    shells = PREVIEW / "shells"
    shells.mkdir(parents=True, exist_ok=True)
    opened = []
    for frag, (page, marker) in PREVIEW_PAGES.items():
        shell = shells / page
        if not shell.exists():
            shell.write_bytes(urllib.request.urlopen(LIVE + page).read())
        html = shell.read_text(encoding="utf-8")
        start = html.index(marker)
        end = html.rindex("</div>", 0, html.index("<footer"))  # closing tag of the page container
        html = html[:start] + (OUT / frag).read_text(encoding="utf-8") + html[end:]
        # Resolve CSS/JS/PDF links against the live site.
        html = html.replace("<head>", f'<head>\n<base href="{LIVE}">', 1)
        out = PREVIEW / page
        out.write_text(html, encoding="utf-8")
        opened.append(str(out))
    subprocess.run(["open", *opened])
    print("Preview:", *opened, sep="\n  ")


def main():
    env = Environment(loader=FileSystemLoader(ROOT / "templates"), keep_trailing_newline=True)
    env.filters["titleize"] = lambda s: " ".join(w.capitalize() for w in s.split())
    entries = load_entries(BIB)
    OUT.mkdir(exist_ok=True)
    for name, ctx in build(entries).items():
        html = env.get_template(name + ".j2").render(no_js=False, **ctx)
        (OUT / name).write_text(html, encoding="utf-8")
    print(f"Built {len(entries)} papers -> {OUT}/")
    if "--preview" in sys.argv:
        preview()


if __name__ == "__main__":
    main()
